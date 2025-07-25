
# -*- coding: utf-8 -*-
import sqlite3
import pandas as pd
conn = sqlite3.connect(DB_PATH)
conn.close()
DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
df = pd.read_sql_query(f"SELECT * FROM {TABLE_NAME} ORDER BY inserted_at DESC", conn)
df.to_csv(EXPORT_PATH, index=False, encoding="utf-8")
EXPORT_PATH = r"C:\BackUp_ehcho_galaxy\logs\export_git_commits_20250501.csv"
TABLE_NAME = "git_commits"
