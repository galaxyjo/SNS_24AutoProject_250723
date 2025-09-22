$ErrorActionPreference = "Stop"
$root = "C:\SNS_24AutoProject_250723"
Set-Location $root
$env:PYTHONPATH = $root

# 1) 로그 정리
New-Item -ItemType Directory -Force -Path "logs" | Out-Null
Remove-Item -Force .coverage -ErrorAction SilentlyContinue
Get-ChildItem -Recurse -Filter "__pycache__" | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force .pytest_cache -ErrorAction SilentlyContinue

# 2) 테스트 실행 + 커버리지 수집
pytest tests/ --maxfail=1 --disable-warnings `
  --cov=modules --cov-report=term-missing `
  --cov-report=json:coverage.json | Tee-Object -FilePath logs/test_log_summary.txt

# 3) CSV 변환
python tools/parse_coverage_json_to_csv.py coverage.json coverage_summary.csv

# 4-1) CSV 헤더 자동 보정
(Get-Content coverage_summary.csv) -replace 'filename', 'file' -replace 'summary_percent', 'percent_covered' | Set-Content coverage_summary.csv

# 5) 기준 검증
python debug_check.py coverage_summary.csv tools/thresholds.yaml
if ($LASTEXITCODE -ne 0) {
  Write-Host "❌ Threshold FAIL"
  exit 1
} else {
  Write-Host "✅ Threshold PASS"
}
