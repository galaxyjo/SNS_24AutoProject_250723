
BACKUP_DIR = r"C:\BackUp_ehcho_galaxy\logs\bak\auto_daily"
csv_backup = os.path.join(BACKUP_DIR, f"logtrace_export_{timestamp}.csv")
db_backup = os.path.join(BACKUP_DIR, f"trace_log_{timestamp}.db")
import datetime
import os
import shutil
os.makedirs(BACKUP_DIR, exist_ok=True)
shutil.copy2(SOURCE_CSV, csv_backup)
shutil.copy2(SOURCE_DB, db_backup)
SOURCE_CSV = r"C:\BackUp_ehcho_galaxy\logs\export_logtrace_20250501.csv"
SOURCE_DB = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
