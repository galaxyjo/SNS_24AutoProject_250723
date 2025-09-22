
"""
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    level TEXT,
    message TEXT,
    session_id TEXT
    timestamp TEXT,
"""
# -*- coding: utf-8 -*-
)
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
conn = sqlite3.connect(db_path)
conn.close()
conn.commit()
CREATE TABLE IF NOT EXISTS logs(
cursor = conn.cursor()
cursor.execute(
db_path=os.path.join(base_dir, "db", "trace_log.db")
import os
import sqlite3

print("??logs ?뚯씠釉??앹꽦 ?먮뒗 ?뺤씤 ?꾨즺")

pass
