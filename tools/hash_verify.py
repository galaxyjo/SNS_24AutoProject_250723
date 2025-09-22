import csv
import hashlib
import os
import sys

# 제외할 확장자 및 디렉토리
EXCLUDE_EXTS = {
    ".env",
    ".yaml",
    ".yml",
    ".svg",
    ".dot",
    ".txt",
    ".md",
    ".json",
    ".log",
    ".iml",
    ".ini",
    ".cfg",
}
EXCLUDE_DIRS = {
    ".git",
    ".venv",
    ".idea",
    "__pycache__",
    "logs",
    "trace",
    "SNS_Snapshots",
    "validator",
    "_testwrite",
    "tests",
}


def is_excluded(path):
    return os.path.splitext(path)[1].lower() in EXCLUDE_EXTS


def file_hash_sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()


def load_hash_map(csv_path):
    hash_to_path = {}
    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            path = row["Path"].replace("\\", "/")
            hash_val = row["Hash"]
            if hash_val and path:
                hash_to_path[hash_val] = path
    return hash_to_path


def verify_hashes(root_dir, hash_map):
    ok, fail = [], []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        for fname in filenames:
            fpath = os.path.join(dirpath, fname)
            if is_excluded(fpath):
                continue
            file_hash = file_hash_sha256(fpath)
            rel_path = os.path.relpath(fpath, root_dir).replace("\\", "/")
            if file_hash not in hash_map:
                fail.append((rel_path, "❌ 해시 불일치 (정답표에 없음)"))
            elif hash_map[file_hash] != rel_path:
                fail.append((rel_path, f"❌ 경로 불일치 → 정답: {hash_map[file_hash]}"))
            else:
                ok.append(rel_path)
    return ok, fail


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python hash_verify.py [root_dir] [hash_csv]")
        sys.exit(1)

    root_dir, hash_csv = sys.argv[1], sys.argv[2]
    hash_map = load_hash_map(hash_csv)
    matched, mismatched = verify_hashes(root_dir, hash_map)

    print(f"\n✅ 정답 위치 & 해시 일치: {len(matched)}개")
    print(f"\n⚠️ 불일치 항목: {len(mismatched)}개")

    for m in matched:
        print(f"    [OK] {m}")

    for m, reason in mismatched:
        print(f"    {reason} → {m}")

    if mismatched:
        sys.exit(1)
    else:
        print("\n🎉 전체 파일이 정확한 위치와 해시로 정답입니다!")
