import pathlib

# 대상 디렉토리
ROOT = pathlib.Path("C:/SNS_24AutoProject_250723")
TARGET_EXT = ".py"

# 2번째 줄에 unexpected indent 가능성 높은 들여쓰기 제거


def clean_indent(path):
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
        if len(lines) >= 2:
            lines[1] = lines[1].lstrip()
            path.write_text("\n".join(lines), encoding="utf-8")
            print(f"✔️ Fixed: {path}")
    except Exception as e:
        print(f"⚠️ Error fixing {path}: {e}")


# 전체 .py 파일 대상 수행
for f in ROOT.rglob(f"*{TARGET_EXT}"):
    if f.is_file() and f.stat().st_size >= 10:
        clean_indent(f)
