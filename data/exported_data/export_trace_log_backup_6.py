
import shutil
import os
import datetime
DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
EXPORT_DIR = r"C:\BackUp_ehcho_galaxy\logs\backup_exports"
export_path = os.path.join(EXPORT_DIR, f"trace_log_backup_{timestamp}.db")
os.makedirs(EXPORT_DIR, exist_ok=True)
shutil.copy2(DB_PATH, export_path)
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
