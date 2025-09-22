import sys
from pathlib import Path


def fix_triple_quotes(filepath):
    path = Path(filepath)
    content = path.read_text(encoding="utf-8")

    triple_double = '"' * 3
    triple_single = "'" * 3

    double_quote_open = content.count(triple_double) % 2 != 0
    single_quote_open = content.count(triple_single) % 2 != 0

    if double_quote_open:
        content += f"\n{triple_double}"
    elif single_quote_open:
        content += f"\n{triple_single}"

    fixed_path = path.with_suffix(".fixed.py")
    fixed_path.write_text(content, encoding="utf-8")
    print(f"✅ fixed: {fixed_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fix_triple_quote.py <path_to_file>")
        sys.exit(1)

    fix_triple_quotes(sys.argv[1])
