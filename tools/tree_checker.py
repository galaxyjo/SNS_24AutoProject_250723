import os

# 경로 설정
MASTER_TREE_PATH = r"C:\path\to\master_tree_0520.txt"  # 기준 트리 txt 경로
TARGET_ROOT_DIR = r"C:\clean_rebuild"  # 실제 디렉토리 경로


def load_master_tree(txt_path):
    expected_paths = set()
    with open(txt_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                expected_paths.add(os.path.normpath(line))
    return expected_paths


def scan_actual_tree(root_dir):
    actual_paths = set()
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            rel_path = os.path.relpath(os.path.join(root, file), root_dir)
            actual_paths.add(os.path.normpath(rel_path))
    return actual_paths


def main():
    print("📥 기준 트리 불러오는 중...")
    expected = load_master_tree(MASTER_TREE_PATH)

    print("🔍 실제 디렉토리 스캔 중...")
    actual = scan_actual_tree(TARGET_ROOT_DIR)

    print("🧾 비교 중...")
    matched = expected & actual
    missing = expected - actual
    extra = actual - expected

    print("\n✅ 일치한 항목 수:", len(matched))
    print("❌ 누락된 항목 수:", len(missing))
    print("⚠️ 추가로 존재하는 이상 항목 수:", len(extra))

    if missing:
        print("\n❌ 누락 항목:")
        for path in sorted(missing):
            print("  [MISSING]", path)

    if extra:
        print("\n⚠️ 예상에 없는 항목:")
        for path in sorted(extra):
            print("  [EXTRA]", path)


if __name__ == "__main__":
    main()
