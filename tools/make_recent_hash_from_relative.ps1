Param(
    [Parameter(Mandatory=$true)]
    [string]$Root,  # e.g. C:\SNS_24AutoProject_250723
    [Parameter(Mandatory=$true)]
    [string]$RecentCsvPath,  # e.g. C:\SNS_24AutoProject_250723\logs\recent_modified_files_48h.csv
    [Parameter(Mandatory=$true)]
    [string]$OutCsvPath  # e.g. C:\SNS_24AutoProject_250723\logs\recent_hash.csv
)

# 1) Load recent modified list (expects column: RelativePath)
$recent = Import-Csv -Path $RecentCsvPath

# 2) Build full paths and keep only files that exist
$rows = @()
foreach ($row in $recent) {
    $rel = $row.RelativePath.Trim()
    if ([string]::IsNullOrWhiteSpace($rel)) { continue }
    $full = Join-Path -Path $Root -ChildPath $rel
    if (Test-Path -LiteralPath $full -PathType Leaf) {
        try {
            $h = Get-FileHash -LiteralPath $full -Algorithm SHA256
            $obj = [PSCustomObject]@{
                filename          = [System.IO.Path]::GetFileName($full)
                current_fullpath  = $full
                sha256            = $h.Hash.ToUpper()
            }
            $rows += $obj
        } catch {
            Write-Warning "Hash fail: $full - $($_.Exception.Message)"
        }
    }
}

# 3) Export
$rows | Export-Csv -Path $OutCsvPath -NoTypeInformation -Encoding UTF8
Write-Host "✅ recent file hashes exported: $OutCsvPath"
