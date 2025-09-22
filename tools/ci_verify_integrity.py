import hashlib
import json
import os
import sys

FINGERPRINT_FILE = r"C:\\SNS_24AutoProject_250723\\integrity_fingerprint_0804.json"
BASE_DIR = r"C:\\SNS_24AutoProject_250723"

with open(FINGERPRINT_FILE, "r", encoding="utf-8") as f:
    original = json.load(f)

errors = []

for path, old_hash in original.items():
    if not os.path.exists(path):
        errors.append(f"[MISSING] {path}")
        continue
    try:
        with open(path, "rb") as f:
            new_hash = hashlib.sha256(f.read()).hexdigest()
        if new_hash != old_hash:
            errors.append(f"[CHANGED] {path}")
    except Exception as e:
        errors.append(f"[ERROR] {path} - {e}")

if errors:
    print("❌ 무결성 검사 실패! 다음 파일을 확인하세요:")
    for e in errors:
        print(e)
    sys.exit(1)
else:
    print("✅ 모든 파일 무결성 통과 (변경 없음)")
