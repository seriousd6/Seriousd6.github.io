<#
.SYNOPSIS
    Push a specific whitelist of local files/folders to the remote Linux machine.

.DESCRIPTION
    Only the items in $SyncItems are ever considered — everything else on both sides
    is ignored entirely. Uploads only new or changed files (compared by size + mtime).

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
    Also delete remote copies of whitelisted files that no longer exist locally.

.EXAMPLE
    .\Sync-ToRemote.ps1
    .\Sync-ToRemote.ps1 -DryRun
    .\Sync-ToRemote.ps1 -DeleteExtra
#>
param(
    [string]  $RemoteHost  = "192.168.86.50",
    [string]  $RemoteUser  = "domad",
    [string]  $RemotePath  = "/home/domad/Documents/bible-study-website",
    [string]  $LocalPath   = "C:\Users\Administrator\Documents\GitHub\Seriousd6.github.io",
    [switch]  $DryRun,
    [switch]  $DeleteExtra = $false
)

$ErrorActionPreference = "Stop"

# Only these items are synced — everything else is ignored on both sides.
# Folder names include all files underneath them recursively.
$SyncItems = @('Z-ExtraResources', 'TODO.md', '.gitignore')

# ── helpers ────────────────────────────────────────────────────────────────────

function Write-Header($msg) {
    Write-Host "`n=== $msg ===" -ForegroundColor Cyan
}

function Test-Included($relPath) {
    foreach ($item in $SyncItems) {
        if ($relPath -eq $item -or $relPath -like "$item\*" -or $relPath -like "$item/*") {
            return $true
        }
    }
    return $false
}

# ── 1. Build local file manifest ──────────────────────────────────────────────

Write-Header "Scanning local files"

$localFiles = [System.Collections.Generic.Dictionary[string, psobject]]::new(
    [System.StringComparer]::OrdinalIgnoreCase
)

if (Test-Path $LocalPath) {
    Get-ChildItem -Path $LocalPath -Recurse -File | ForEach-Object {
        $relPath = $_.FullName.Substring($LocalPath.TrimEnd('\').Length).TrimStart('\')
        if (Test-Included $relPath) {
            $epochUtc = ([System.DateTimeOffset]::new($_.LastWriteTimeUtc)).ToUnixTimeMilliseconds() / 1000.0
            $localFiles[$relPath] = [pscustomobject]@{
                FullPath  = $_.FullName
                Timestamp = $epochUtc
                Size      = $_.Length
            }
        }
    }
}

Write-Host "Local:  $($localFiles.Count) files found (syncing: $($SyncItems -join ', '))"

# ── 2. Fetch remote file manifest for whitelisted paths only ──────────────────

Write-Header "Fetching remote file list from $RemoteUser@$RemoteHost"

# Build a targeted find that only checks the whitelisted items on the remote.
# Dirs get a recursive find; root-level files get a -maxdepth 1 name match.
$findParts = $SyncItems | ForEach-Object {
    $localItem = Join-Path $LocalPath $_
    if (Test-Path $localItem -PathType Container) {
        "find . -path './$_/*' -type f -printf '%P\t%T@\t%s\n' 2>/dev/null"
    } else {
        "find . -maxdepth 1 -name '$_' -type f -printf '%P\t%T@\t%s\n' 2>/dev/null"
    }
}
$findCmd = "cd '$RemotePath' && { $($findParts -join '; '); } | sort"

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
    $parts = $line -split "`t", 3
    if ($parts.Count -ne 3) { continue }

    $relPath = $parts[0] -replace '/', '\'

    $remoteFiles[$relPath] = [pscustomobject]@{
        Timestamp = [double]$parts[1]
        Size      = [long]$parts[2]
    }
}

Write-Host "Remote: $($remoteFiles.Count) files found (within synced paths)"

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
    } else {
        $remote   = $remoteFiles[$relPath]
        $timeDiff = [Math]::Abs($local.Timestamp - $remote.Timestamp)

        if ($local.Size -ne $remote.Size -or $timeDiff -gt 2) {
            Write-Host "  CHANGED $relPath" -ForegroundColor Yellow
            $toUpload.Add($relPath)
        } else {
            $unchanged++
        }
    }
}

# Remote files in the whitelist that no longer exist locally
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
        $stdoutTask = $proc.StandardOutput.ReadToEndAsync()

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

# ── 5. Delete remote-only whitelisted files (opt-in) ──────────────────────────

if ($DeleteExtra -and $remoteOnlyCount -gt 0) {
    Write-Header "Deleting $remoteOnlyCount remote-only files"

    foreach ($f in $remoteOnly) {
        $remoteFile = $RemotePath + '/' + ($f -replace '\\', '/')
        ssh "${RemoteUser}@${RemoteHost}" "rm -f '$remoteFile'"
        Write-Host "  DELETED $f" -ForegroundColor Red
    }

    # Remove empty directories left behind within whitelisted paths only
    $syncUnix = ($SyncItems | ForEach-Object { "$RemotePath/$_" }) -join ' '
    $cleanCmd = "find $syncUnix -type d -empty -delete 2>/dev/null"
    ssh "${RemoteUser}@${RemoteHost}" $cleanCmd
    Write-Host "  Empty directories removed." -ForegroundColor DarkRed
}

# ── Done ──────────────────────────────────────────────────────────────────────

Write-Header "Done"
Write-Host "Uploaded: $($toUpload.Count)  |  Remote-only: $remoteOnlyCount  |  Unchanged: $unchanged"
