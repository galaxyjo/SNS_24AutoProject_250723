# tools/apply_fixed_files.ps1
# 모든 .fixed.py 파일을 원본 .py로 덮어쓰기
# 덮어쓰기 전/후 로그 기록 및 오류 처리 포함

$ErrorActionPreference = "Stop"

# 현재 경로 기준 모든 .fixed.py 탐색
Get-ChildItem -Recurse -Filter "*.fixed.py" | ForEach-Object {
    $fixedPath = $_.FullName
    $originalPath = $fixedPath -replace '\.fixed\.py$', '.py'

    if (Test-Path $originalPath) {
        try {
            Copy-Item -Path $fixedPath -Destination $originalPath -Force
            Write-Host "🔄 replaced: $originalPath"
        } catch {
            Write-Host "❌ 오류 발생 (복사 실패): $originalPath"
        }
    } else {
        Write-Host "⚠️ 원본 없음, 새로 생성됨: $originalPath"
        try {
            Copy-Item -Path $fixedPath -Destination $originalPath -Force
        } catch {
            Write-Host "❌ 오류 발생 (생성 실패): $originalPath"
        }
    }
}

Write-Host "✅ 모든 .fixed.py → .py 교체 작업 완료"
