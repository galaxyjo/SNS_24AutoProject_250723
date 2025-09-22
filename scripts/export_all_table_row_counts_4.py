import datetime
import sqlite3

import pandas as pd

DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
EXPORT_PATH = (
    r"C:\BackUp_ehcho_galaxy\logs\export_all_tables_"
    + datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    + ".csv"
)

conn = sqlite3.connect(DB_PATH)
tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", conn)

with open(EXPORT_PATH, "w", newline="", encoding="utf-8") as f:
    f.write("Table Name, Row Count\n")
    for table in tables["name"]:
        df = pd.read_sql_query(f"SELECT COUNT(*) FROM {table}", conn)
        count = df.iloc[0, 0]
        f.write(f"{table}, {count}\n")

conn.close()
