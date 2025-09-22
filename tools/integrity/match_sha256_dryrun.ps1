# PowerShell Script: match_sha256_dryrun.ps1

# 📁 파일 경로 정의
$unmatchedFile = "C:\SNS_24AutoProject_250723\tools\integrity\unmatched_files_with_hash0808_1651.csv"
$hashReference = "C:\SNS_24AutoProject_250723\tools\integrity\sha256_list.20250723_1618.csv"
$outputFile    = "C:\SNS_24AutoProject_250723\tools\integrity\matched_files_preview.csv"
$logFile       = "C:\SNS_24AutoProject_250723\tools\integrity\match_log.txt"
$previewLimit  = 5

# 📌 기준 CSV 확인
if (-not (Test-Path $hashReference)) {
    Write-Error "❌ 기준 해시 CSV 없음: $hashReference"
    return
}
if (-not (Test-Path $unmatchedFile)) {
    Write-Error "❌ 비교 대상 CSV 없음: $unmatchedFile"
    return
}

# 📥 CSV 로드
try {
    $unmatchedData = Import-Csv -Path $unmatchedFile
    $referenceData = Import-Csv -Path $hashReference
} catch {
    Write-Error "❌ CSV 파일 로드 실패: $_"
    return
}

# 🧠 기준 해시 딕셔너리 생성
$hashTable = @{}
foreach ($ref in $referenceData) {
    if ($ref.sha256 -and $ref.filename) {
        $key = "$($ref.filename)|$($ref.sha256)"
        $hashTable[$key] = $ref.full_path
    }
}

# ✅ 매핑
$matched = @()
foreach ($row in $unmatchedData) {
    if (-not $row.Filename -or -not $row.SHA256) {
        Add-Content -Path $logFile -Value "⚠️ 누락 정보 → $($row.FullPath)"
        continue
    }

    $key = "$($row.Filename)|$($row.SHA256)"
    if ($hashTable.ContainsKey($key)) {
        $matched += [PSCustomObject]@{
            Filename     = $row.Filename
            SHA256       = $row.SHA256
            FullPath     = $row.FullPath
            MatchedPath  = $hashTable[$key]
        }
    }
}

# 👁 미리보기
$matched | Select-Object -First $previewLimit | Format-Table | Out-String -Width 200 | Write-Host

# 💾 중복 경고
if (Test-Path $outputFile) {
    Write-Warning "⚠️ 기존 파일 존재: $outputFile → 덮어쓰기 예정"
}

# 💾 저장
$matched | Export-Csv -Path $outputFile -NoTypeInformation -Encoding UTF8

# 🧾 로그
"[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] 매핑 완료: $($matched.Count)건 / 미리보기 $previewLimit건 저장됨 → $outputFile" | Out-File -Append -FilePath $logFile
