
                '.txt', '.md', '.json', '.log', '.iml', '.ini', '.cfg'}
                continue
                fail.append((rel_path, "❌ 해시 불일치 (정답표에 없음)"))
                fail.append((rel_path, f"❌ 경로 불일치 → 정답: {hash_map[file_hash]}"))
                hash_to_path[hash_val] = path
                ok.append(rel_path)
                'trace', 'SNS_Snapshots', 'validator', '_testwrite', 'tests'}
            elif hash_map[file_hash] != rel_path:
            else:
            file_hash = file_hash_sha256(fpath)
            fpath = os.path.join(dirpath, fname)
            h.update(chunk)
            hash_val = row['Hash']
            if file_hash not in hash_map:
            if hash_val and path:
            if is_excluded(fpath):
            path = row['Path'].replace("\\", "/")
            print(f"    {reason} → {m}")
            rel_path = os.path.relpath(fpath, root_dir).replace("\\", "/")
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        for chunk in iter(lambda: f.read(4096), b""):
        for fname in filenames:
        for m, reason in mismatched:
        for row in reader:
        print("\n🎉 전체 파일이 정확한 위치와 해시로 정답입니다!")
        print("Usage: python hash_verify_strict_v2.py [root_dir] [hash_csv]")
        print(f"    [OK] {m}")
        print(f"\n⚠️ 불일치 항목: {len(mismatched)}개")
        reader = csv.DictReader(csvfile)
        sys.exit(1)
    else:
    for dirpath, dirnames, filenames in os.walk(root_dir):
    for m in matched:
    h = hashlib.sha256()
    hash_map = load_hash_map(hash_csv)
    hash_to_path = {}
    if len(sys.argv) != 3:
    if mismatched:
    matched, mismatched = verify_hashes(root_dir, hash_map)
    ok, fail = [], []
    print(f"\n✅ 정답 위치 & 해시 일치: {len(matched)}개")
    return h.hexdigest()
    return hash_to_path
    return ok, fail
    return os.path.splitext(path)[1].lower() in EXCLUDE_EXTS
    root_dir, hash_csv = sys.argv[1], sys.argv[2]
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
    with open(path, "rb") as f:
def file_hash_sha256(path):
def is_excluded(path):
def load_hash_map(csv_path):
def verify_hashes(root_dir, hash_map):
EXCLUDE_DIRS = {'.git', '.venv', '.idea', '__pycache__', 'logs',
EXCLUDE_EXTS = {'.env', '.yaml', '.yml', '.svg', '.dot',
if __name__ == "__main__":
import csv
import hashlib
import os
import sys
