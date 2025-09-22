# -*- coding: utf-8 -*-
import datetime
import sqlite3

DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
BACKUP_DIR = r"C:\BackUp_ehcho_galaxy\logs\bak\full_db_backups"

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
backup_file = os.path.join(BACKUP_DIR, f"trace_log_full_backup_{timestamp}.db")

os.makedirs(BACKUP_DIR, exist_ok=True)

conn = sqlite3.connect(DB_PATH)
conn.backup(open(backup_file, "wb"))
conn.close()
