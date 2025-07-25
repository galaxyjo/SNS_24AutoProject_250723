
                break
                hash_val = sha256sum(file_path)
                print(f"Warning: File not found - {file_path}")
                results.append([file_path, hash_val])
            chunk = f.read(8192)
            else:
            file_path = os.path.join(base_path, file_rel_path)
            h.update(chunk)
            if not chunk:
            if os.path.isfile(file_path):
        for file_rel_path in file_list:
        while True:
        writer = csv.writer(csvfile)
        writer.writerow(["file_path", "sha256"])
        writer.writerows(results)
    "core/main_features.py",
    "launcher/main.py",
    "modules/account_runner.py",
    "modules/test_account_runner.py",
    "src/config/settings.py",
    "src/main.py",
    "src/models/schema.py",
    "src/routes/api.py",
    "src/services/data_service.py",
    "src/utils/helpers.py"
    for base_path in base_paths:
    generate_hash_csv(base_paths, file_list, output_csv)
    h = hashlib.sha256()
    now = datetime.now().strftime("%Y%m%d")
    output_csv = f"master_hash_rebuild_{now}.csv"
    print(f"Hash CSV saved to {output_file}")
    r"C:\clean_rebuild_recovery",
    r"C:\clean_rebuild\backup"
    results = []
    return h.hexdigest()
    with open(filename, 'rb') as f:
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
# 1. 기준 경로 리스트
# 2. 기준 파일 목록
# 3. SHA256 해시 함수
# 4. 해시 생성 및 CSV 저장
]
base_paths = [
def generate_hash_csv(base_paths, file_list, output_file):
def sha256sum(filename):
file_list = [
from datetime import datetime
if __name__ == "__main__":
import csv
import hashlib
import os
