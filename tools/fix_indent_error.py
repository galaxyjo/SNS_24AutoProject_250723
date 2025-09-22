"""
🔧 fix_indent_error.py
- 대상: IndentationError
- 전략: 잘못된 인덴트 (예: Tab + Space 혼용)를 전부 Space(4칸)로 통일
"""

from pathlib import Path


def fix_indent(file_path):
    fixed_lines = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            new_line = line.replace("\t", "    ")
            fixed_lines.append(new_line)

    fixed_path = file_path.with_suffix(".fixed.py")
    with open(fixed_path, "w", encoding="utf-8") as f:
        f.writelines(fixed_lines)
    return fixed_path


if __name__ == "__main__":
    import sys

    for target in sys.argv[1:]:
        fixed = fix_indent(Path(target))
        print(f"✅ fixed: {fixed}")
