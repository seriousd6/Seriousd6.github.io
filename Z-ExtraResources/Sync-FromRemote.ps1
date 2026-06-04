<#
.SYNOPSIS
    Sync a remote Linux directory to a local Windows path, copying only new or changed files.

.DESCRIPTION
    Compares remote files (by size + mtime) against local files and downloads only what differs.
    Leaves local-only files (e.g. .git) untouched unless -DeleteExtra is specified.

.PARAMETER RemoteHost
    IP or hostname of the remote machine. Default: 192.168.86.50

.PARAMETER RemoteUser
    SSH username. Default: domad

.PARAMETER RemotePath
    Absolute path on the remote to sync FROM. Default: /home/domad/Documents/bible-study-website

.PARAMETER LocalPath
    Local path to sync INTO. Default: current repo root.

.PARAMETER DryRun
    Show what would change without touching any files.

.PARAMETER DeleteExtra
    Also delete local files that no longer exist on the remote.
    WARNING: does NOT delete files in excluded directories (e.g. .git).

.EXAMPLE
    .\Sync-FromRemote.ps1
    .\Sync-FromRemote.ps1 -DryRun
    .\Sync-FromRemote.ps1 -DeleteExtra
#>
param(
    [string]  $RemoteHost  = "192.168.86.50",
    [string]  $RemoteUser  = "domad",
    [string]  $RemotePath  = "/home/domad/Documents/bible-study-website",
    [string]  $LocalPath   = "C:\Users\Administrator\Documents\GitHub\Seriousd6.github.io",
    [switch]  $DryRun = $false,
    [switch]  $DeleteExtra = $false
)

$ErrorActionPreference = "Stop"

# Directories to ignore on both sides (never downloaded, never deleted)
$ExcludeDirs = @('.git', 'node_modules', '.claude')

# ── helpers ────────────────────────────────────────────────────────────────────

function Write-Header($msg) {
    Write-Host "`n=== $msg ===" -ForegroundColor Cyan
}

function Is-Excluded($relPath) {
    foreach ($dir in $ExcludeDirs) {
        if ($relPath -like "$dir\*" -or $relPath -like "$dir/*" -or $relPath -eq $dir) {
            return $true
        }
    }
    return $false
}

# ── 1. Fetch remote file manifest via SSH ─────────────────────────────────────

Write-Header "Fetching remote file list from $RemoteUser@$RemoteHost"

# Build find command using -prune to skip excluded directories entirely.
# This avoids descending into them and handles both top-level and nested cases.
$pruneExpr = ($ExcludeDirs | ForEach-Object { "-name '$_'" }) -join ' -o '
$findCmd = "find '$RemotePath' \( -type d \( $pruneExpr \) -prune \) -o \( -type f -printf '%P\t%T@\t%s\n' \) 2>/dev/null | sort"

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

    # Normalise path separators to Windows backslash
    $relPath = $parts[0] -replace '/', '\'

    $remoteFiles[$relPath] = [pscustomobject]@{
        Timestamp = [double]$parts[1]
        Size      = [long]$parts[2]
    }
}

Write-Host "Remote: $($remoteFiles.Count) files found"

# ── 2. Build local file manifest ──────────────────────────────────────────────

Write-Header "Scanning local files"

$localFiles = [System.Collections.Generic.Dictionary[string, psobject]]::new(
    [System.StringComparer]::OrdinalIgnoreCase
)

if (Test-Path $LocalPath) {
    Get-ChildItem -Path $LocalPath -Recurse -File | ForEach-Object {
        $relPath = $_.FullName.Substring($LocalPath.TrimEnd('\').Length).TrimStart('\')
        if (-not (Is-Excluded $relPath)) {
            $epochUtc = ([System.DateTimeOffset]::new($_.LastWriteTimeUtc)).ToUnixTimeMilliseconds() / 1000.0
            $localFiles[$relPath] = [pscustomobject]@{
                FullPath  = $_.FullName
                Timestamp = $epochUtc
                Size      = $_.Length
            }
        }
    }
}

Write-Host "Local:  $($localFiles.Count) files found (excluding: $($ExcludeDirs -join ', '))"

# ── 3. Diff ────────────────────────────────────────────────────────────────────

Write-Header "Comparing"

$toDownload  = [System.Collections.Generic.List[string]]::new()
$unchanged   = 0

foreach ($kvp in $remoteFiles.GetEnumerator()) {
    $relPath = $kvp.Key
    $remote  = $kvp.Value

    if (-not $localFiles.ContainsKey($relPath)) {
        Write-Host "  NEW     $relPath" -ForegroundColor Green
        $toDownload.Add($relPath)
    } else {
        $local = $localFiles[$relPath]
        $timeDiff = [Math]::Abs($remote.Timestamp - $local.Timestamp)

        # 2-second tolerance covers NTFS/ext4 rounding differences
        if ($remote.Size -ne $local.Size -or $timeDiff -gt 2) {
            Write-Host "  CHANGED $relPath" -ForegroundColor Yellow
            $toDownload.Add($relPath)
        } else {
            $unchanged++
        }
    }
}

# Files that exist locally but not on the remote
$localOnly = $localFiles.Keys | Where-Object { -not $remoteFiles.ContainsKey($_) }
foreach ($f in $localOnly) {
    Write-Host "  LOCAL   $f" -ForegroundColor DarkGray
}

$localOnlyCount = @($localOnly).Count

Write-Host ""
Write-Host "  To download  : $($toDownload.Count)" -ForegroundColor White
Write-Host "  Unchanged    : $unchanged"            -ForegroundColor White
Write-Host "  Local-only   : $localOnlyCount"       -ForegroundColor White

if ($DryRun) {
    Write-Host "`n[DRY RUN] No files were modified." -ForegroundColor Magenta
    exit 0
}

if ($toDownload.Count -eq 0 -and (-not $DeleteExtra -or $localOnlyCount -eq 0)) {
    Write-Host "`nAlready up to date." -ForegroundColor Green
    exit 0
}

# ── 4. Download changed / new files ───────────────────────────────────────────
# Uses a single SSH connection: we pipe the file list to `tar --files-from=-`
# on the remote, stream the tar archive back over stdout, then extract locally.
# One connection = one password prompt (or none with key auth).

if ($toDownload.Count -gt 0) {
    Write-Header "Downloading $($toDownload.Count) files via single SSH connection"

    $tempTar = Join-Path $env:TEMP "bsw_sync_$([System.IO.Path]::GetRandomFileName()).tar.gz"

    try {
        # Launch SSH: remote side reads file list from stdin, tars those files to stdout.
        # We redirect stdin/stdout through .NET streams to handle binary data correctly —
        # PowerShell's pipeline would corrupt binary content by re-encoding it as text.
        $psi = [System.Diagnostics.ProcessStartInfo]::new("ssh")
        $psi.Arguments          = "${RemoteUser}@${RemoteHost} `"cd '$RemotePath' && tar czf - --files-from=-`""
        $psi.RedirectStandardInput  = $true
        $psi.RedirectStandardOutput = $true
        $psi.RedirectStandardError  = $true
        $psi.UseShellExecute        = $false

        $proc = [System.Diagnostics.Process]::Start($psi)

        # Read stderr async so it never blocks the stdout pipe
        $stderrTask = $proc.StandardError.ReadToEndAsync()

        # Build the file list as a raw UTF-8 byte array with LF-only line endings,
        # then write directly to the underlying BaseStream. This completely bypasses
        # StreamWriter's NewLine/encoding logic, which was stripping path separators.
        $fileListStr   = ($toDownload | ForEach-Object { $_ -replace '\\', '/' }) -join "`n"
        $fileListBytes = [System.Text.Encoding]::UTF8.GetBytes($fileListStr + "`n")
        $proc.StandardInput.BaseStream.Write($fileListBytes, 0, $fileListBytes.Length)
        $proc.StandardInput.BaseStream.Flush()
        $proc.StandardInput.BaseStream.Close()

        # Stream binary stdout directly to a temp file — no text encoding involved
        $outStream = [System.IO.FileStream]::new($tempTar, [System.IO.FileMode]::Create)
        $proc.StandardOutput.BaseStream.CopyTo($outStream)
        $outStream.Close()

        $stderr = $stderrTask.Result
        $proc.WaitForExit()

        if ($proc.ExitCode -ne 0) {
            Write-Error "Remote tar failed (exit $($proc.ExitCode)):`n$stderr"
        } else {
            if ($stderr) { Write-Host "  SSH: $stderr" -ForegroundColor DarkGray }

            Write-Host "  Extracting..."
            $tarOut = tar xzf $tempTar -C $LocalPath 2>&1
            if ($LASTEXITCODE -ne 0) {
                Write-Error "Local tar extraction failed:`n$tarOut"
            } else {
                Write-Host "  $($toDownload.Count) files extracted successfully." -ForegroundColor Green
            }
        }
    } finally {
        if (Test-Path $tempTar) { Remove-Item $tempTar -Force }
    }
}

# ── 5. Delete local-only files (opt-in) ───────────────────────────────────────

if ($DeleteExtra -and $localOnlyCount -gt 0) {
    Write-Header "Deleting $localOnlyCount local-only files"

    foreach ($f in $localOnly) {
        $fullPath = Join-Path $LocalPath $f
        Remove-Item $fullPath -Force
        Write-Host "  DELETED $f" -ForegroundColor Red
    }

    # Clean up empty directories left behind (skip excluded dirs)
    Get-ChildItem -Path $LocalPath -Recurse -Directory |
        Sort-Object FullName -Descending |
        Where-Object {
            $relDir = $_.FullName.Substring($LocalPath.TrimEnd('\').Length).TrimStart('\')
            -not (Is-Excluded $relDir) -and
            @(Get-ChildItem $_.FullName -Force).Count -eq 0
        } |
        ForEach-Object {
            Remove-Item $_.FullName -Force
            Write-Host "  RMDIR   $($_.FullName.Substring($LocalPath.Length+1))" -ForegroundColor DarkRed
        }
}

# ── Done ──────────────────────────────────────────────────────────────────────

Write-Header "Done"
Write-Host "Downloaded: $($toDownload.Count)  |  Local-only: $localOnlyCount  |  Unchanged: $unchanged"
