Add-Type -AssemblyName System.IO.Compression.FileSystem

$zipPath = "c:\Users\GC\Documents\TBB\TBB\Website planning\Wordpress Files Backup\public_html.zip"
$destBase = "c:\Users\GC\Documents\TBB\astro\public\images"

$zip = [System.IO.Compression.ZipFile]::OpenRead($zipPath)

$imageEntries = $zip.Entries | Where-Object {
    $_.FullName -like "wp-content/uploads/*" -and
    $_.Length -gt 0 -and
    $_.FullName -match "\.(png|jpg|jpeg|gif|webp|svg)$"
}

Write-Host "Found $($imageEntries.Count) image files to extract"

foreach ($entry in $imageEntries) {
    # Strip "wp-content/uploads/" prefix to get relative path
    $relativePath = $entry.FullName -replace "^wp-content/uploads/", ""
    $destPath = Join-Path $destBase $relativePath

    # Create directory if needed
    $destDir = Split-Path $destPath -Parent
    if (-not (Test-Path $destDir)) {
        New-Item -ItemType Directory -Path $destDir -Force | Out-Null
    }

    # Extract file
    [System.IO.Compression.ZipFileExtensions]::ExtractToFile($entry, $destPath, $true)
    Write-Host "  Extracted: $relativePath"
}

$zip.Dispose()
Write-Host "`nDone! Extracted $($imageEntries.Count) images to $destBase"
