
        columns, columns = ["cid", "name", "type", "notnull", "dflt_value", "pk"]
    )
    columns = cur.fetchall()
    cur.execute(f"PRAGMA table_info({table_name})")
    df = pd.DataFrame(
    df.to_csv(export_path, index=False, encoding="utf-8")
    export_path = os.path.join(EXPORT_DIR, f"{table_name}_schema.csv")
    table_name = table[0]
# -*- coding: utf-8 -*-
conn = sqlite3.connect(DB_PATH)
conn.close()
cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
EXPORT_DIR = r"C:\BackUp_ehcho_galaxy\logs\schema_exports"
for table in tables:
import os
import pandas as pd
import sqlite3
os.makedirs(EXPORT_DIR, exist_ok=True)
tables = cur.fetchall()
