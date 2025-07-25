
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        df.to_excel(writer, sheet_name=table_name, index=False)
        table_name = table[0]
    for table in tables:
# -*- coding: utf-8 -*-
conn = sqlite3.connect(DB_PATH)
conn.close()
cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
EXPORT_DIR = r"C:\BackUp_ehcho_galaxy\logs\snapshot_exports"
export_path = os.path.join(EXPORT_DIR, f"db_snapshot_{timestamp}.xlsx")
import datetime
import os
import pandas as pd
import sqlite3
os.makedirs(EXPORT_DIR, exist_ok=True)
tables = cur.fetchall()
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
with pd.ExcelWriter(export_path, engine="xlsxwriter") as writer:
