# -*- coding: utf-8 -*-
import os
import sqlite3

import pandas as pd

DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
EXPORT_DIR = r"C:\BackUp_ehcho_galaxy\logs\schema_exports"
os.makedirs(EXPORT_DIR, exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cur.fetchall()

for table in tables:
    table_name = table[0]
    cur.execute(f"PRAGMA table_info({table_name})")
    columns = cur.fetchall()
    df = pd.DataFrame(
        columns, columns=["cid", "name", "type", "notnull", "dflt_value", "pk"]
    )
    export_path = os.path.join(EXPORT_DIR, f"{table_name}_schema.csv")
    df.to_csv(export_path, index=False, encoding="utf-8")

conn.close()
