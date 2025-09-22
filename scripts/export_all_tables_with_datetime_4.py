import datetime
import os
import sqlite3

import pandas as pd

DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
EXPORT_DIR = r"C:\BackUp_ehcho_galaxy\logs\exports"
os.makedirs(EXPORT_DIR, exist_ok=True)

EXPORT_PATH = os.path.join(
    EXPORT_DIR,
    "export_all_tables_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".xlsx",
)

conn = sqlite3.connect(DB_PATH)
tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", conn)

with pd.ExcelWriter(EXPORT_PATH, engine="xlsxwriter") as writer:
    for table in tables["name"]:
        df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
        df.to_excel(writer, sheet_name=table, index=False)

conn.close()
