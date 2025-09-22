# tools/fix_all_error_files.ps1
# black_failed_files.txt 목록을 기준으로 fix_*.py 스크립트 자동 실행
# 각 오류 유형별 수리 스크립트를 순차 실행하며, 결과 로그를 기록

$ErrorActionPreference = "Stop"

# 오류 파일 목록 불러오기
$files = Get-Content "black_failed_files.txt"

foreach ($file in $files) {
    if (Test-Path $file) {
        Write-Host "🔧 수리 중: $file"

        try {
            python tools/fix_triple_quote.py $file
        } catch {
            Write-Host "❌ fix_triple_quote 실패: $file"
        }

        try {
            python tools/fix_indent_error.py $file
        } catch {
            Write-Host "❌ fix_indent_error 실패: $file"
        }

        try {
            python tools/fix_eof_block.py $file
        } catch {
            Write-Host "❌ fix_eof_block 실패: $file"
        }

    } else {
        Write-Host "❌ 파일 없음: $file"
    }
}

Write-Host "✅ 모든 오류 수리 스크립트 실행 완료"
