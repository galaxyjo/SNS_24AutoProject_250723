import datetime
import sqlite3

import pandas as pd

DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
EXPORT_PATH = (
    r"C:\BackUp_ehcho_galaxy\logs\log_summary_"
    + datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    + ".csv"
)

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cur.fetchall()

with open(EXPORT_PATH, "w", newline="", encoding="utf-8") as f:
    f.write("Table Name, Row Count\n")
    for table in tables:
        table_name = table[0]
        cur.execute(f"SELECT COUNT(*) FROM {table_name}")
        count = cur.fetchone()[0]
        f.write(f"{table_name}, {count}\n")

conn.close()
