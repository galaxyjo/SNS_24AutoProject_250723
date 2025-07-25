
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            level TEXT,
            message TEXT,
            session_id TEXT
            timestamp TEXT,
        """
        );
        CREATE TABLE logs (
    """
    )
    cur.execute(
    INSERT INTO logs (timestamp, level, message, session_id)
    print("??logs ?뚯씠釉??앹꽦 ?꾨즺")
    print("??logs ?뚯씠釉?議댁옱 ?뺤씤")
    print(row)
    VALUES ('2025-05-05 21:30:00', 'INFO', 'Streamlit ?뚯뒪??濡쒓렇 ?쎌엯', 'session_test')
"""
# -*- coding: utf-8 -*-
# ?뚯씪 ?꾩튂: C:\SNS_24AutoProject\scripts\check_and_insert_log.py
# 1. DB ?곌껐
# 2. logs ?뚯씠釉?議댁옱 ?щ? ?뺤씤
# 3. ?덉퐫??媛쒖닔 議고쉶
# 4. ?뚯뒪??濡쒓렇 1嫄??쎌엯
# 5. ?꾩껜 濡쒓렇 異쒕젰
)
BASE_PATH = os.getenv("BASE_PATH")
conn = sqlite3.connect(db_path)
conn.close()
conn.commit()
count = cur.fetchone()[0]
cur = conn.cursor()
cur.execute(
cur.execute("SELECT * FROM logs;")
cur.execute("SELECT COUNT(*) FROM logs;")
cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='logs';")
DB_PATH = os.getenv("DB_PATH")
db_path = os.path.join(os.path.dirname(__file__), "..", "db", "trace_log.db")
else:
EXPORT_PATH = os.getenv("EXPORT_PATH")
for row in rows:
from dotenv import load_dotenv
if not cur.fetchone():
import os
import sqlite3
import sys
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
LOG_PATH = os.getenv("LOG_PATH")
MODULE_PATH = os.getenv("MODULE_PATH")
os.chdir(BASE_PATH)
print("???뚯뒪??濡쒓렇 ?쎌엯 ?꾨즺")
print("?뱥 ?꾩껜 濡쒓렇:")
print(f"?벀 ?꾩옱 濡쒓렇 ?덉퐫???? {count}")
rows = cur.fetchall()
sys.path.append(MODULE_PATH)
