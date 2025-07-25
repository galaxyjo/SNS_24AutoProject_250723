
# -*- coding: utf-8 -*-
import sys
import sqlite3
import pandas as pd
import os
from dotenv import load_dotenv
BASE_PATH = os.getenv("BASE_PATH")
conn = sqlite3.connect(DB_PATH)
conn.close()
DB_PATH = os.getenv("DB_PATH")
DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
df = pd.read_sql_query(f"SELECT * FROM {TABLE_NAME} ORDER BY executed_at DESC", conn)
df.to_csv(EXPORT_PATH, index=False, encoding="utf-8")
EXPORT_PATH = os.getenv("EXPORT_PATH")
EXPORT_PATH = r"C:\BackUp_ehcho_galaxy\logs\export_hook_logs_20250501.csv"
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
LOG_PATH = os.getenv("LOG_PATH")
MODULE_PATH = os.getenv("MODULE_PATH")
os.chdir(BASE_PATH)
sys.path.append(MODULE_PATH)
TABLE_NAME = "hook_logs"
