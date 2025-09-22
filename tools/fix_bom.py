# fix_bom.py - 전체 .py 파일 대상 BOM 제거 스크립트
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TARGET_EXT = ".py"
SKIP_DIRS = {".venv", "venv", "__pycache__", ".git", "logs", "output"}


def find_py_files(base_dir):
    for root, dirs, files in os.walk(base_dir):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for file in files:
            if file.endswith(TARGET_EXT):
                yield os.path.join(root, file)


def remove_bom(file_path):
    try:
        with open(file_path, "r", encoding="utf-8-sig") as f:
            content = f.read()
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[OK] BOM 제거 완료 → {file_path}")
    except Exception as e:
        print(f"[ERR] {file_path} 처리 중 오류: {e}")


if __name__ == "__main__":
    print(f"🔍 루트 경로 검색 시작: {ROOT_DIR}")
    for py_file in find_py_files(ROOT_DIR):
        remove_bom(py_file)
