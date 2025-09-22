
arcname = os.path.relpath(full_path, TARGET_DIR)
                full_path = os.path.join(root, file)
                zipf.write(full_path, arcname)
            if file.endswith(".db") or file.endswith(".csv") or file.endswith(".xlsx"):
        for file in files:
    f'log_backup_bundle_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.zip'
    for root, dirs, files in os.walk(TARGET_DIR):
)
EXPORT_NAME = (
EXPORT_PATH = os.path.join(TARGET_DIR, EXPORT_NAME)
import datetime
import os
import zipfile

TARGET_DIR = r"C:\BackUp_ehcho_galaxy\logs"
with zipfile.ZipFile(EXPORT_PATH, "w", zipfile.ZIP_DEFLATED) as zipf:
