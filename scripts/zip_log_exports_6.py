# scripts/zip_log_exports_6.py
import os
import datetime
import zipfile


def zip_logs(target_dir: str, export_path: str = None) -> str:
    if not os.path.exists(target_dir):
        raise FileNotFoundError(f"⚠️ Target directory does not exist: {target_dir}")

    if export_path is None:
        export_name = f'log_backup_bundle_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.zip'
        export_path = os.path.join(target_dir, export_name)

    with zipfile.ZipFile(export_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(target_dir):
            for file in files:
                if file.endswith((".db", ".csv", ".xlsx")):
                    full_path = os.path.join(root, file)
                    arcname = os.path.relpath(full_path, target_dir)
                    zipf.write(full_path, arcname)
    print(f"✅ Logs zipped to: {export_path}")
    return export_path


def main():
    target_dir = os.getenv("EXPORT_PATH") or r"C:\BackUp_ehcho_galaxy\logs"
    zip_logs(target_dir)


if __name__ == "__main__":
    main()
