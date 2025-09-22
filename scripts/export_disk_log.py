# -*- coding: utf-8 -*-
import os
import sys

from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
BASE_PATH = os.getenv("BASE_PATH")
DB_PATH = os.getenv("DB_PATH")
LOG_PATH = os.getenv("LOG_PATH")
EXPORT_PATH = os.getenv("EXPORT_PATH")
MODULE_PATH = os.getenv("MODULE_PATH")
sys.path.append(MODULE_PATH)
os.chdir(BASE_PATH)
import os

# scripts/export_disk_log.py
import sqlite3
from datetime import datetime

import pandas as pd

conn = sqlite3.connect("db/disk_log.db")
df = pd.read_sql_query("SELECT * FROM disk_log ORDER BY id DESC", conn)
conn.close()

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
export_path = os.path.join("logs", f"export_disk_log_{timestamp}.csv")
df.to_csv(export_path, index=False, encoding="utf-8-sig")

print(f"??Export complete: {export_path}")
