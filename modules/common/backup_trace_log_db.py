import datetime
import os
import shutil
import sqlite3

DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
BACKUP_DIR = r"C:\BackUp_ehcho_galaxy\logs\bak\db_backups"

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
backup_file = os.path.join(BACKUP_DIR, f"trace_log_backup_{timestamp}.db")

os.makedirs(BACKUP_DIR, exist_ok=True)

shutil.copy2(DB_PATH, backup_file)
