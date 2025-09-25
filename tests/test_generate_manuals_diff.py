# tests/test_generate_manuals_diff.py
from pathlib import Path
from scripts.ci_tools import generate_manuals

def test_manuals_md_diff(tmp_path):
    # 1. 테스트용 출력 경로
    output_path = tmp_path / "manuals_test.md"
    
    # 2. 실제 파일 생성
    generate_manuals.generate_manual(str(output_path))  # 함수 내부 인자 타입이 str이면 str로 변환

    # 3. 비교 대상 읽기
    expected_path = Path("docs/manuals_latest.md")
    assert expected_path.exists(), "Expected manual (manuals_latest.md) not found."

    expected = expected_path.read_text(encoding="utf-8")
    actual = output_path.read_text(encoding="utf-8")

    # 4. 내용 비교
    assert expected == actual, "Generated manual differs from latest baseline."
