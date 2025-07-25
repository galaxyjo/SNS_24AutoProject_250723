
        ["file_name", "function_name", "desc", "GPT_REF", "STEP", "inserted_at"]
    )
    f"SELECT file_name, function_name, desc, GPT_REF, STEP, inserted_at FROM {TABLE_NAME}"
    writer = csv.writer(f)
    writer.writerow(
    writer.writerows(rows)
)
conn = sqlite3.connect(DB_PATH)
conn.close()
CSV_EXPORT_PATH = r"C:\BackUp_ehcho_galaxy\logs\export_logtrace_20250501.csv"
cur = conn.cursor()
cur.execute(
DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
import csv
import sqlite3
rows = cur.fetchall()
TABLE_NAME = "log_trace"
with open(CSV_EXPORT_PATH, "w", newline="", encoding="utf-8") as f:
