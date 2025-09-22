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
