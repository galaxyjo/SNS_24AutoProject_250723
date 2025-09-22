
(r["file_name"], r["function_name"], r["desc"], r["GPT_REF"], r["STEP"])
        for r in reader
    ]
    desc TEXT,
    f"""
    file_name TEXT,
    function_name TEXT,
    GPT_REF TEXT,
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    inserted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    reader = csv.DictReader(f)
    rows = [
    rows,
    STEP TEXT,
"""
""",
# -*- coding: utf-8 -*-
)
conn = sqlite3.connect(db_path)
conn.close()
conn.commit()
CREATE TABLE IF NOT EXISTS {table_name} (
csv_path = os.path.join("logs", "insert_log_2025-05-01.csv")
cur = conn.cursor()
cur.execute(
cur.executemany(
db_path = "trace_log.db"
import csv
import os
import sqlite3
INSERT INTO {table_name} (file_name, function_name, desc, GPT_REF, STEP)
table_name = "log_trace"
VALUES (?, ?, ?, ?, ?)
with open(csv_path, encoding="utf-8") as f:
