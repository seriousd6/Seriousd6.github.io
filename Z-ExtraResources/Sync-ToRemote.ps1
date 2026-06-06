<#
.SYNOPSIS
    Push all local files to the remote Linux machine, skipping only excluded dirs/files.

.DESCRIPTION
    Compares local files against the remote (by MD5 hash, or size+mtime with -SkipHash)
    and uploads only what is new or changed. Remote-only files are reported but left alone
    unless -DeleteExtra is specified.

.PARAMETER RemoteHost
    IP or hostname of the remote machine. Default: 192.168.86.50

.PARAMETER RemoteUser
    SSH username. Default: domad

.PARAMETER RemotePath
    Absolute path on the remote to sync INTO. Default: /home/domad/Documents/bible-study-website

.PARAMETER LocalPath
    Local path to sync FROM. Default: current repo root.

.PARAMETER DryRun
    Show what would change without touching any files.

.PARAMETER DeleteExtra
    Also delete remote files that no longer exist locally (within non-excluded paths).

.PARAMETER Target
    Optional file or directory to sync. Accepts an absolute path or a path relative to
    LocalPath (e.g. "topics\john" or "assets\css\style.css"). When omitted, all files
    are considered (subject to ExcludeDirs / ExcludeFiles).

.PARAMETER SkipHash
    Fall back to size+mtime comparison instead of MD5 hash comparison.
    Faster but can produce false positives when timestamps drift across platforms.

.EXAMPLE
    .\Sync-ToRemote.ps1
    .\Sync-ToRemote.ps1 -DryRun
    .\Sync-ToRemote.ps1 -Target topics\john
    .\Sync-ToRemote.ps1 -Target "assets\css\style.css" -DryRun:$false
    .\Sync-ToRemote.ps1 -DeleteExtra
    .\Sync-ToRemote.ps1 -SkipHash
#>
param(
    [string]  $RemoteHost  = "192.168.86.50",
    [string]  $RemoteUser  = "domad",
    [string]  $RemotePath  = "/home/domad/Documents/bible-study-website",
    [string]  $LocalPath   = "C:\Users\Administrator\Documents\GitHub\Seriousd6.github.io",
    [string]  $Target      = "C:\Users\Administrator\Documents\GitHub\Seriousd6.github.io\Z_AGENT_PROMPT.md",
    [switch]  $DryRun      = $false,
    [switch]  $DeleteExtra = $false,
    [switch]  $SkipHash    = $false
)

$ErrorActionPreference = "Stop"

# Directories to ignore on both sides (never uploaded, never deleted)
$ExcludeDirs = @('.git', 'node_modules', '.claude')

# Individual files to ignore on both sides — matched by filename anywhere in the tree
$ExcludeFiles = @('.gitattributes')

# ── resolve -Target to a repo-relative backslash path ─────────────────────────

$TargetRel = ""
if ($Target) {
    $t = $Target.Trim()
    if ([System.IO.Path]::IsPathRooted($t)) {
        $lpTrimmed = $LocalPath.TrimEnd('\')
        if (-not $t.StartsWith($lpTrimmed, [System.StringComparison]::OrdinalIgnoreCase)) {
            Write-Error "-Target '$t' is not under LocalPath '$LocalPath'"
            exit 1
        }
        $t = $t.Substring($lpTrimmed.Length)
    }
    $TargetRel = ($t.TrimStart('\').TrimStart('/')) -replace '/', '\'
    if (-not $TargetRel) {
        Write-Error "-Target resolved to an empty path — pass a file or subdirectory."
        exit 1
    }
}

# ── helpers ────────────────────────────────────────────────────────────────────

function Write-Header($msg) {
    Write-Host "`n=== $msg ===" -ForegroundColor Cyan
}

# Returns true when relPath should be included given the active -Target (if any).
function Test-InTarget($relPath) {
    if (-not $TargetRel) { return $true }
    return ($relPath -eq $TargetRel -or $relPath -like "$TargetRel\*")
}

function Test-Excluded($relPath) {
    foreach ($dir in $ExcludeDirs) {
        if ($relPath -like "$dir\*" -or $relPath -like "$dir/*" -or $relPath -eq $dir) {
            return $true
        }
    }
    $leaf = Split-Path $relPath -Leaf
    foreach ($file in $ExcludeFiles) {
        if ($leaf -eq $file) { return $true }
    }
    return $false
}

# ── 1. Build local file manifest ──────────────────────────────────────────────

$hashMode = -not $SkipHash
$targetLabel = if ($TargetRel) { " → $TargetRel" } else { "" }
Write-Header "Scanning local files$targetLabel$(if ($hashMode) { ' (MD5 mode)' } else { ' (size+mtime mode)' })"

$localFiles = [System.Collections.Generic.Dictionary[string, psobject]]::new(
    [System.StringComparer]::OrdinalIgnoreCase
)

$scanRoot = if ($TargetRel) { Join-Path $LocalPath $TargetRel } else { $LocalPath }

if (Test-Path $scanRoot) {
    Get-ChildItem -Path $scanRoot -Recurse -File | ForEach-Object {
        $relPath = $_.FullName.Substring($LocalPath.TrimEnd('\').Length).TrimStart('\')
        if (-not (Test-Excluded $relPath) -and (Test-InTarget $relPath)) {
            if ($hashMode) {
                $hash = (Get-FileHash $_.FullName -Algorithm MD5).Hash.ToLower()
                $localFiles[$relPath] = [pscustomobject]@{
                    FullPath = $_.FullName
                    Hash     = $hash
                }
            } else {
                $epochUtc = ([System.DateTimeOffset]::new($_.LastWriteTimeUtc)).ToUnixTimeMilliseconds() / 1000.0
                $localFiles[$relPath] = [pscustomobject]@{
                    FullPath  = $_.FullName
                    Timestamp = $epochUtc
                    Size      = $_.Length
                }
            }
        }
    }
}

$scopeNote = if ($TargetRel) { "target: $TargetRel" } else { "excluding dirs: $($ExcludeDirs -join ', '); files: $($ExcludeFiles -join ', ')" }
Write-Host "Local:  $($localFiles.Count) files found ($scopeNote)"

# ── 2. Fetch remote file manifest via SSH ─────────────────────────────────────

Write-Header "Fetching remote file list from $RemoteUser@$RemoteHost$targetLabel"

$pruneExpr = ($ExcludeDirs | ForEach-Object { "-name '$_'" }) -join ' -o '

if ($hashMode) {
    # cd first so md5sum emits relative paths; -print0 + xargs -0 handles any filename safely
    $findCmd = "cd '$RemotePath' && find . \( -type d \( $pruneExpr \) -prune \) -o \( -type f -print0 \) 2>/dev/null | xargs -0 md5sum 2>/dev/null | sort -k2"
} else {
    $findCmd = "cd '$RemotePath' && find . \( -type d \( $pruneExpr \) -prune \) -o \( -type f -printf '%P\t%T@\t%s\n' \) 2>/dev/null | sort"
}

try {
    $remoteLines = ssh "${RemoteUser}@${RemoteHost}" $findCmd
} catch {
    Write-Error "SSH connection failed. Is the remote machine reachable and is SSH key auth set up?`n$_"
    exit 1
}

$remoteFiles = [System.Collections.Generic.Dictionary[string, psobject]]::new(
    [System.StringComparer]::OrdinalIgnoreCase
)

foreach ($line in $remoteLines) {
    if ([string]::IsNullOrWhiteSpace($line)) { continue }

    if ($hashMode) {
        # md5sum output: "<hash>  ./relpath" (two spaces between hash and path)
        if ($line -notmatch '^([0-9a-fA-F]{32})\s+\.?[/\\]?(.+)$') { continue }
        $relPath = ($Matches[2] -replace '/', '\').TrimStart('\')
        if (Test-Excluded $relPath) { continue }
        if (-not (Test-InTarget $relPath)) { continue }
        $remoteFiles[$relPath] = [pscustomobject]@{ Hash = $Matches[1].ToLower() }
    } else {
        $parts = $line -split "`t", 3
        if ($parts.Count -ne 3) { continue }
        $relPath = $parts[0] -replace '/', '\'
        if (Test-Excluded $relPath) { continue }
        if (-not (Test-InTarget $relPath)) { continue }
        $remoteFiles[$relPath] = [pscustomobject]@{
            Timestamp = [double]$parts[1]
            Size      = [long]$parts[2]
        }
    }
}

Write-Host "Remote: $($remoteFiles.Count) files found"

# ── 3. Diff ────────────────────────────────────────────────────────────────────

Write-Header "Comparing"

$toUpload  = [System.Collections.Generic.List[string]]::new()
$unchanged = 0

foreach ($kvp in $localFiles.GetEnumerator()) {
    $relPath = $kvp.Key
    $local   = $kvp.Value

    if (-not $remoteFiles.ContainsKey($relPath)) {
        Write-Host "  NEW     $relPath" -ForegroundColor Green
        $toUpload.Add($relPath)
    } elseif ($hashMode) {
        if ($local.Hash -ne $remoteFiles[$relPath].Hash) {
            Write-Host "  CHANGED $relPath  (local: $($local.Hash.Substring(0,8))…  remote: $($remoteFiles[$relPath].Hash.Substring(0,8))…)" -ForegroundColor Yellow
            $toUpload.Add($relPath)
        } else {
            $unchanged++
        }
    } else {
        $remote   = $remoteFiles[$relPath]
        $timeDiff = [Math]::Abs($local.Timestamp - $remote.Timestamp)
        # 2-second tolerance covers NTFS/ext4 rounding differences
        if ($local.Size -ne $remote.Size -or $timeDiff -gt 2) {
            Write-Host "  CHANGED $relPath" -ForegroundColor Yellow
            $toUpload.Add($relPath)
        } else {
            $unchanged++
        }
    }
}

# Files that exist on remote but not locally
$remoteOnly = $remoteFiles.Keys | Where-Object { -not $localFiles.ContainsKey($_) }
foreach ($f in $remoteOnly) {
    Write-Host "  REMOTE  $f" -ForegroundColor DarkGray
}

$remoteOnlyCount = @($remoteOnly).Count

Write-Host ""
Write-Host "  To upload    : $($toUpload.Count)"  -ForegroundColor White
Write-Host "  Unchanged    : $unchanged"           -ForegroundColor White
Write-Host "  Remote-only  : $remoteOnlyCount"     -ForegroundColor White

if ($DryRun) {
    Write-Host "`n[DRY RUN] No files were modified." -ForegroundColor Magenta
    exit 0
}

if ($toUpload.Count -eq 0 -and (-not $DeleteExtra -or $remoteOnlyCount -eq 0)) {
    Write-Host "`nAlready up to date." -ForegroundColor Green
    exit 0
}

# ── 4. Upload changed / new files ─────────────────────────────────────────────
# Create a local tar archive from the changed file list, then stream it to the
# remote over a single SSH connection for extraction. One connection = one prompt.

if ($toUpload.Count -gt 0) {
    Write-Header "Uploading $($toUpload.Count) files via single SSH connection"

    $tempTar      = Join-Path $env:TEMP "bsw_push_$([System.IO.Path]::GetRandomFileName()).tar.gz"
    $tempFileList = Join-Path $env:TEMP "bsw_push_files_$([System.IO.Path]::GetRandomFileName()).txt"

    try {
        # Write file list (Unix paths, LF-terminated) for tar --files-from
        $fileListStr   = ($toUpload | ForEach-Object { $_ -replace '\\', '/' }) -join "`n"
        $fileListBytes = [System.Text.Encoding]::UTF8.GetBytes($fileListStr + "`n")
        [System.IO.File]::WriteAllBytes($tempFileList, $fileListBytes)

        Write-Host "  Creating local archive..."
        $tarOut = tar czf $tempTar -C $LocalPath --files-from=$tempFileList 2>&1
        if ($LASTEXITCODE -ne 0) {
            Write-Error "Local tar creation failed:`n$tarOut"
        }

        Write-Host "  Streaming archive to remote..."

        # Open SSH: remote extracts tar from stdin
        $psi = [System.Diagnostics.ProcessStartInfo]::new("ssh")
        $psi.Arguments              = "${RemoteUser}@${RemoteHost} `"cd '$RemotePath' && tar xzf -`""
        $psi.RedirectStandardInput  = $true
        $psi.RedirectStandardOutput = $true
        $psi.RedirectStandardError  = $true
        $psi.UseShellExecute        = $false

        $proc = [System.Diagnostics.Process]::Start($psi)

        $stderrTask = $proc.StandardError.ReadToEndAsync()

        # Write archive bytes directly to SSH stdin — no text re-encoding
        $tarBytes = [System.IO.File]::ReadAllBytes($tempTar)
        $proc.StandardInput.BaseStream.Write($tarBytes, 0, $tarBytes.Length)
        $proc.StandardInput.BaseStream.Flush()
        $proc.StandardInput.BaseStream.Close()

        $proc.WaitForExit()
        $stderr = $stderrTask.Result

        if ($proc.ExitCode -ne 0) {
            Write-Error "Remote tar extraction failed (exit $($proc.ExitCode)):`n$stderr"
        } else {
            if ($stderr) { Write-Host "  SSH: $stderr" -ForegroundColor DarkGray }
            Write-Host "  $($toUpload.Count) files uploaded successfully." -ForegroundColor Green
        }
    } finally {
        if (Test-Path $tempTar)      { Remove-Item $tempTar      -Force }
        if (Test-Path $tempFileList) { Remove-Item $tempFileList -Force }
    }
}

# ── 5. Delete remote-only files (opt-in) ──────────────────────────────────────

if ($DeleteExtra -and $remoteOnlyCount -gt 0) {
    Write-Header "Deleting $remoteOnlyCount remote-only files"

    foreach ($f in $remoteOnly) {
        $remoteFile = $RemotePath + '/' + ($f -replace '\\', '/')
        ssh "${RemoteUser}@${RemoteHost}" "rm -f '$remoteFile'"
        Write-Host "  DELETED $f" -ForegroundColor Red
    }

    # Remove empty directories left behind within non-excluded paths only
    $cleanCmd = "cd '$RemotePath' && find . \( -type d \( $pruneExpr \) -prune \) -o \( -type d -empty -print \) 2>/dev/null | sort -r | xargs -r rmdir 2>/dev/null; true"
    ssh "${RemoteUser}@${RemoteHost}" $cleanCmd
    Write-Host "  Empty directories removed." -ForegroundColor DarkRed
}

# ── Done ──────────────────────────────────────────────────────────────────────

Write-Header "Done"
Write-Host "Uploaded: $($toUpload.Count)  |  Remote-only: $remoteOnlyCount  |  Unchanged: $unchanged"
