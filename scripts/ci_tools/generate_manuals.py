# C:\SNS_24AutoProject_250723\scripts\ci_tools\generate_manuals.py
import os
from pathlib import Path

__all__ = ["generate_manuals"]

DEFAULT_CONTENT = "# 자동 생성 매뉴얼\n\n자동 생성된 매뉴얼 내용입니다.\n"

def generate_manuals(output_path=None, content: str = DEFAULT_CONTENT) -> str:
    """
    manuals.md 생성 + 내용 반환 (CI/테스트용 고정 콘텐츠)
    """
    output_path = (
        Path(__file__).parent.parent.parent / "docs" / "manuals.md"
        if output_path is None else Path(output_path)
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")
    return content

def main():
    # CLI 실행 시 docs/manuals.md 생성
    generate_manuals()

if __name__ == "__main__":
    main()
