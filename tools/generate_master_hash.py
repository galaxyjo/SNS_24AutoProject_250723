import csv
import hashlib
import os
from datetime import datetime

# 1. 기준 경로 리스트
base_paths = [r"C:\clean_rebuild_recovery", r"C:\clean_rebuild\backup"]

# 2. 기준 파일 목록
file_list = [
    "core/main_features.py",
    "launcher/main.py",
    "modules/account_runner.py",
    "modules/test_account_runner.py",
    "src/config/settings.py",
    "src/main.py",
    "src/models/schema.py",
    "src/routes/api.py",
    "src/services/data_service.py",
    "src/utils/helpers.py",
]


# 3. SHA256 해시 함수
def sha256sum(filename):
    h = hashlib.sha256()
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


# 4. 해시 생성 및 CSV 저장
def generate_hash_csv(base_paths, file_list, output_file):
    results = []
    for base_path in base_paths:
        for file_rel_path in file_list:
            file_path = os.path.join(base_path, file_rel_path)
            if os.path.isfile(file_path):
                hash_val = sha256sum(file_path)
                results.append([file_path, hash_val])
            else:
                print(f"Warning: File not found - {file_path}")

    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["file_path", "sha256"])
        writer.writerows(results)


if __name__ == "__main__":
    now = datetime.now().strftime("%Y%m%d")
    output_csv = f"master_hash_rebuild_{now}.csv"
    generate_hash_csv(base_paths, file_list, output_csv)
    print(f"Hash CSV saved to {output_csv}")
