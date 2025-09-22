import argparse
import csv
import hashlib
import json
import os

mastertree_map = {
    "main.py": "launcher",
    "run_engine.py": "core",
    "task_router.py": "core",
    "log_initializer.py": "core",
    "error_handler.py": "core",
    "account_runner.py": "modules",
    "logger.py": "modules/common",
    "asyncio_custom.py": "modules/common",
    # ... 나머지 필요한 파일들도 여기에 추가
}


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()


def load_hash_map(csv_path):
    mapping = {}
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            path = row.get("filename") or row.get("file") or row.get("Path")
            sha = (
                row.get("sha256")
                or row.get("SHA256")
                or row.get("hash")
                or row.get("Hash")
            )
            if sha and path:
                rel_path = path.strip().replace("\\", "/")
                mapping[rel_path] = sha.strip().lower()
    return mapping


def scan_py_files(root):
    py_files = []
    for dirpath, _, filenames in os.walk(root):
        for f in filenames:
            if f.endswith(".py"):
                py_files.append(os.path.join(dirpath, f))
    return py_files


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hash-map", required=True)
    parser.add_argument("--root", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--target-root", default="C:/SNS_24AutoProject")
    args = parser.parse_args()

    hash_map = load_hash_map(args.hash_map)
    files = scan_py_files(args.root)

    result = []
    for f in files:
        sha = sha256_file(f).lower()
        rel_path = os.path.relpath(f, args.root).replace("\\", "/")
        fname = os.path.basename(f)

        if rel_path in hash_map:
            if hash_map[rel_path] != sha:
                print(f"[❌] 기준 해시와 경로 불일치: {rel_path}")
                continue
        else:
            print(f"[⚠️] 기준 해시표에 없음: {rel_path}")
            continue

        subdir = mastertree_map.get(fname)
        if subdir:
            target_path = os.path.join(args.target_root, subdir, fname)
        else:
            print(f"[⚠️] mastertree 경로 없음: {fname}")
            target_path = os.path.join(args.target_root, "UNMAPPED", fname)

        result.append(
            {
                "source": os.path.abspath(f),
                "target": os.path.normpath(target_path),
                "sha256": sha,
            }
        )

    with open(args.out, "w", encoding="utf-8") as out_f:
        json.dump(result, out_f, indent=2)

    print(f"\n✅ 이동 대상 {len(result)}개 → {args.out}")


if __name__ == "__main__":
    main()
