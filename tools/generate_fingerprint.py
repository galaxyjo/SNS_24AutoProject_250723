import hashlib
import json
import os

fingerprints = {}
base_dir = r"C:\\SNS_24AutoProject_250723"

for root, _, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".py"):
            full_path = os.path.join(root, file)
            try:
                with open(full_path, "rb") as f:
                    file_bytes = f.read()
                    sha256 = hashlib.sha256(file_bytes).hexdigest()
                    fingerprints[full_path] = sha256
            except Exception as e:
                fingerprints[full_path] = f"ERROR: {e}"

with open(
    os.path.join(base_dir, "integrity_fingerprint_0804.json"), "w", encoding="utf-8"
) as f:
    json.dump(fingerprints, f, indent=2)
