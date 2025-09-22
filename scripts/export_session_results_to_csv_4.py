import sqlite3

import pandas as pd

DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
EXPORT_PATH = r"C:\BackUp_ehcho_galaxy\logs\export_session_results_20250501.csv"
TABLE_NAME = "session_results"

conn = sqlite3.connect(DB_PATH)
df = pd.read_sql_query(f"SELECT * FROM {TABLE_NAME} ORDER BY executed_at DESC", conn)
conn.close()

df.to_csv(EXPORT_PATH, index=False, encoding="utf-8")
