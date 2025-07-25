
                expected_paths.add(os.path.normpath(line))
            actual_paths.add(os.path.normpath(rel_path))
            if line and not line.startswith("#"):
            line = line.strip()
            print("  [EXTRA]", path)
            print("  [MISSING]", path)
            rel_path = os.path.relpath(os.path.join(root, file), root_dir)
        for file in files:
        for line in f:
        for path in sorted(extra):
        for path in sorted(missing):
        print("\n❌ 누락 항목:")
        print("\n⚠️ 예상에 없는 항목:")
    actual = scan_actual_tree(TARGET_ROOT_DIR)
    actual_paths = set()
    expected = load_master_tree(MASTER_TREE_PATH)
    expected_paths = set()
    extra = actual - expected
    for root, dirs, files in os.walk(root_dir):
    if extra:
    if missing:
    main()
    matched = expected & actual
    missing = expected - actual
    print("\n✅ 일치한 항목 수:", len(matched))
    print("❌ 누락된 항목 수:", len(missing))
    print("⚠️ 추가로 존재하는 이상 항목 수:", len(extra))
    print("📥 기준 트리 불러오는 중...")
    print("🔍 실제 디렉토리 스캔 중...")
    print("🧾 비교 중...")
    return actual_paths
    return expected_paths
    with open(txt_path, "r", encoding="utf-8") as f:
# tree_checker.py
def load_master_tree(txt_path):
def main():
def scan_actual_tree(root_dir):
if __name__ == "__main__":
import os
MASTER_TREE_PATH = r"C:\path\to\master_tree_0520.txt"  # 기준 트리 txt 경로
TARGET_ROOT_DIR = r"C:\clean_rebuild"  # 실제 디렉토리 경로
