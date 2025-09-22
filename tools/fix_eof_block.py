"""
🔧 fix_eof_block.py
- 대상: unexpected EOF / SyntaxError: expected ':'
- 전략: 열린 괄호, 열린 if/def 등 닫히지 않은 블록에 대해 pass 또는 닫기 추가
"""

from pathlib import Path


def fix_eof_block(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if lines and not lines[-1].strip().endswith((":", "pass")):
        lines.append("\npass\n")

    fixed_path = file_path.with_suffix(".fixed.py")
    with open(fixed_path, "w", encoding="utf-8") as f:
        f.writelines(lines)
    return fixed_path


if __name__ == "__main__":
    import sys

    for target in sys.argv[1:]:
        fixed = fix_eof_block(Path(target))
        print(f"✅ fixed: {fixed}")
