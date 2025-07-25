
        df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
        df.to_excel(writer, sheet_name=table, index=False)
    "export_all_tables_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".xlsx",
    EXPORT_DIR,
    for table in tables["name"]:
)
conn = sqlite3.connect(DB_PATH)
conn.close()
DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
EXPORT_DIR = r"C:\BackUp_ehcho_galaxy\logs\exports"
EXPORT_PATH = os.path.join(
import datetime
import os
import pandas as pd
import sqlite3
os.makedirs(EXPORT_DIR, exist_ok=True)
tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", conn)
with pd.ExcelWriter(EXPORT_PATH, engine="xlsxwriter") as writer:
