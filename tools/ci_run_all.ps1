# ✅ 1. 환경 고정
$env:PYTHONPATH = "C:\SNS_24AutoProject_250723"
$python = ".venv\Scripts\python.exe"
$timestamp = Get-Date -Format "yyyyMMdd_HHmm"

# ✅ 2. 폴더 준비
New-Item -ItemType Directory -Force -Path "coverage" | Out-Null
New-Item -ItemType Directory -Force -Path "logs\summary" | Out-Null

# ✅ 3. 테스트 실행 + 커버리지 저장
& $python -m pytest tests `
    --cov=modules `
    --cov-report=json:coverage\coverage.json `
    --cov-report=term `
    --maxfail=3 --disable-warnings

# ✅ 4. 커버리지 요약 CSV 변환
& $python tools\coverage_utils\parse_coverage_json_to_csv.py `
    coverage\coverage.json `
    coverage\coverage_summary_$timestamp.csv

# ✅ 5. 린트 점검 (Pylint)
& $python -m pylint launcher modules `
    --output-format=parseable `
    > logs\summary\pylint_report_$timestamp.txt

# ✅ 6. 커버리지 CSV 복사 요약 저장
Copy-Item "coverage\coverage_summary_$timestamp.csv" "logs\summary\coverage_summary_latest.csv" -Force

Write-Host "`n✅ CI/CD 자동 실행 완료 ($timestamp)"
