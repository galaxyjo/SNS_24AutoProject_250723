# C:\SNS_24AutoProject_250723\tests\test_ci_tools\test_generate_manuals.py
import os
from pathlib import Path
from scripts.ci_tools import generate_manuals

# 기준 파일 경로 (동일 유지)
BASELINE_PATH = Path("scripts/ci_tools/manuals_20250925.md")

def test_manuals_md_auto_update(tmp_path):
    # 임시 출력 경로 (테스트용)
    test_output_path = tmp_path / "manuals.md"

    # generate_manuals 실행 후 내용 추출
    generated_content = generate_manuals.generate_manuals(output_path=test_output_path)

    # 기준 파일 없으면 처음 생성
    if not BASELINE_PATH.exists():
        BASELINE_PATH.write_text(generated_content, encoding="utf-8")
        assert BASELINE_PATH.exists(), "기준 파일이 새로 생성되지 않았습니다."
        return

    # 기준 내용 읽기
    baseline_content = BASELINE_PATH.read_text(encoding="utf-8")

    # 비교 후 다를 경우 기준 업데이트
    if generated_content != baseline_content:
        BASELINE_PATH.write_text(generated_content, encoding="utf-8")
        raise AssertionError("📌 manuals_20250925.md 파일이 업데이트되었습니다. 기준이 변경되었습니다.")
