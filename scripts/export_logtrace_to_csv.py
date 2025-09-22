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
import csv
import os
import sqlite3

DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
CSV_EXPORT_PATH = r"C:\BackUp_ehcho_galaxy\logs\export_logtrace_20250501.csv"
TABLE_NAME = "log_trace"

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
cur.execute(
    f"SELECT file_name, function_name, desc, GPT_REF, STEP, inserted_at FROM {TABLE_NAME}"
)
rows = cur.fetchall()
conn.close()

with open(CSV_EXPORT_PATH, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(
        ["file_name", "function_name", "desc", "GPT_REF", "STEP", "inserted_at"]
    )
    writer.writerows(rows)
