# scripts/create_release_zip.py
# ===============================
# 출처: create_release_zip.py
import os, zipfile

def create_release_zip():
    base_dir = "C:\\SNS_24AutoProject"
    output_zip = "C:\\backup_Release.zip"
    with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
        for folder in ["configs","dashboards","db","decorators","docs","logs","modules","scripts","static"]:
            folder_path = os.path.join(base_dir, folder)
            for root, _, files in os.walk(folder_path):
                for file in files:
                    full_path = os.path.join(root, file)
                    arcname = os.path.relpath(full_path, base_dir)
                    zipf.write(full_path, arcname=arcname)
        zipf.write(os.path.join(base_dir, "main.py"), arcname="main.py")
        zipf.write(os.path.join(base_dir, "insert_logtrace_auto.ps1"), arcname="insert_logtrace_auto.ps1")
    print(f"✅ 배포용 패키지 생성 완료: {output_zip}")

if __name__ == "__main__":
    create_release_zip()
