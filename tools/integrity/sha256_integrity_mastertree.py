# sha256_integrity_mastertree.py (모드 강제 선택 수정)
import csv
import hashlib
import json
import os
from datetime import datetime


def calculate_sha256(file_path):
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()


def get_files(root):
    file_list = []
    for dirpath, _, filenames in os.walk(root):
        for f in filenames:
            file_list.append(os.path.join(dirpath, f))
    return file_list


def generate_baseline(root):
    hashes = {
        os.path.relpath(path, root): calculate_sha256(path) for path in get_files(root)
    }
    baseline_file = os.path.join(root, "master_hashes.json")
    with open(baseline_file, "w", encoding="utf-8") as f:
        json.dump(hashes, f, indent=4, ensure_ascii=False)
    print(f"✅ 기준 해시 생성 완료: {baseline_file}")


def verify_integrity(root, baseline_file):
    with open(baseline_file, "r", encoding="utf-8") as f:
        baseline = json.load(f)

    current = {
        os.path.relpath(path, root): calculate_sha256(path) for path in get_files(root)
    }
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    csv_file = os.path.join(root, f"hash_verify_{timestamp}.csv")

    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["RelativePath", "FullPath", "SHA256", "Status"])
        for rel, hash_now in current.items():
            status = (
                "OK"
                if rel in baseline and hash_now == baseline[rel]
                else ("CHANGED" if rel in baseline else "NEW")
            )
            writer.writerow([rel, os.path.join(root, rel), hash_now, status])
        for rel in baseline:
            if rel not in current:
                writer.writerow([rel, "(삭제됨)", baseline[rel], "DELETED"])
    print(f"✅ 무결성 검증 완료: {csv_file}")


if __name__ == "__main__":
    root = input("📂 프로젝트 루트 경로 입력: ").strip()
    mode = input("모드 선택 (1=기준 해시 생성 / 2=무결성 검증): ").strip()
    if mode == "1":
        generate_baseline(root)
    elif mode == "2":
        baseline = input("📄 기준 해시 파일 경로 입력: ").strip()
        verify_integrity(root, baseline)
    else:
        print("❌ 잘못된 모드 입력")
