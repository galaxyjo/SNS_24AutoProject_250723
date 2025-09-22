
import os
import sqlite3
import sys

from dotenv import load_dotenv

"INSERT OR IGNORE INTO users (username, password, role) VALUES ('viewer1', 'test1234', 'viewer')"
# -*- coding: utf-8 -*-
# ?꾩튂: C:\SNS_24AutoProject\scripts\insert_viewer_user.py
# ?뚯씪紐? insert_viewer_user.py
)
    BASE_PATH = os.getenv("BASE_PATH")
    conn = sqlite3.connect(db_path)
    conn.close()
    conn.commit()
    cur = conn.cursor()
    cur.execute(
DB_PATH = os.getenv("DB_PATH")
db_path = os.path.join(os.path.dirname(__file__), "..", "db", "session_log.db")
EXPORT_PATH = os.getenv("EXPORT_PATH")
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
LOG_PATH = os.getenv("LOG_PATH")
MODULE_PATH = os.getenv("MODULE_PATH")
os.chdir(BASE_PATH)
print("??viewer1 怨꾩젙 ?앹꽦 ?꾨즺 (鍮꾨?踰덊샇: test1234, 沅뚰븳: viewer)")
sys.path.append(MODULE_PATH)

pass
