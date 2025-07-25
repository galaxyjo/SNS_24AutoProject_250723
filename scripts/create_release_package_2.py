
                arcname = os.path.relpath(full_path, base_dir)
                full_path = os.path.join(root, file)
                zipf.write(full_path, arcname=arcname)
            for file in files:
        "configs",
        "dashboards",
        "db",
        "decorators",
        "docs",
        "logs",
        "modules",
        "scripts",
        "static",
        arcname="insert_logtrace_auto.ps1",
        folder_path = os.path.join(base_dir, folder)
        for root, _, files in os.walk(folder_path):
        os.path.join(base_dir, "insert_logtrace_auto.ps1"),
    )
    ]:
    for folder in [
    zipf.write(
    zipf.write(os.path.join(base_dir, "main.py"), arcname="main.py")
base_dir = "C:\\SNS_24AutoProject"
import os
import zipfile
output_zip = "C:\\backup_2025-05-06_Release.zip"
print(f"✅ 배포용 패키지 생성 완료: {output_zip}")
with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
