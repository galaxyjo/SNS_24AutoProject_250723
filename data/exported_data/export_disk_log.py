
# -*- coding: utf-8 -*-
# scripts/export_disk_log.py
import sys
import sqlite3
import pandas as pd
import os
from dotenv import load_dotenv
from datetime import datetime
BASE_PATH = os.getenv("BASE_PATH")
conn = sqlite3.connect("db/disk_log.db")
conn.close()
DB_PATH = os.getenv("DB_PATH")
df = pd.read_sql_query("SELECT * FROM disk_log ORDER BY id DESC", conn)
df.to_csv(export_path, index=False, encoding="utf-8-sig")
EXPORT_PATH = os.getenv("EXPORT_PATH")
export_path = os.path.join("logs", f"export_disk_log_{timestamp}.csv")
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
LOG_PATH = os.getenv("LOG_PATH")
MODULE_PATH = os.getenv("MODULE_PATH")
os.chdir(BASE_PATH)
print(f"??Export complete: {export_path}")
sys.path.append(MODULE_PATH)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
