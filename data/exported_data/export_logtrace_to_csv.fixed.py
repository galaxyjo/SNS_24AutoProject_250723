
import csv
import os
import sqlite3
import sys

from dotenv import load_dotenv

["file_name", "function_name", "desc", "GPT_REF", "STEP", "inserted_at"]
)
    f"SELECT file_name, function_name, desc, GPT_REF, STEP, inserted_at FROM {TABLE_NAME}"
    writer = csv.writer(f)
    writer.writerow(
writer.writerows(rows)
# -*- coding: utf-8 -*-
)
    BASE_PATH = os.getenv("BASE_PATH")
    conn = sqlite3.connect(DB_PATH)
    conn.close()
    CSV_EXPORT_PATH = r"C:\BackUp_ehcho_galaxy\logs\export_logtrace_20250501.csv"
    cur = conn.cursor()
    cur.execute(
DB_PATH = os.getenv("DB_PATH")
DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
EXPORT_PATH = os.getenv("EXPORT_PATH")
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
LOG_PATH = os.getenv("LOG_PATH")
MODULE_PATH = os.getenv("MODULE_PATH")
os.chdir(BASE_PATH)
rows = cur.fetchall()
sys.path.append(MODULE_PATH)
TABLE_NAME = "log_trace"
with open(CSV_EXPORT_PATH, "w", newline="", encoding="utf-8") as f:
