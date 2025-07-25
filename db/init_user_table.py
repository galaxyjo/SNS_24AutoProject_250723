
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        password TEXT,
        role TEXT DEFAULT 'viewer'
        username TEXT UNIQUE,
    """
    "INSERT OR IGNORE INTO users (username, password, role) VALUES (?, ?, ?)",
    ("admin", "1234", "admin"),
    );
    CREATE TABLE IF NOT EXISTS users (
"""
# -*- coding: utf-8 -*-
# ?덈? 寃쎈줈 湲곗? DB ?곌껐
# ?뚯씪紐? init_user_table.py
# admin 怨꾩젙 ?깅줉
# users ?뚯씠釉??앹꽦
# 紐⑹쟻: user_credentials.db??users ?뚯씠釉??앹꽦 諛?admin 怨꾩젙 ?깅줉
)
BASE_PATH = os.getenv("BASE_PATH")
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
conn = sqlite3.connect(db_path)
conn.close()
conn.commit()
cur = conn.cursor()
cur.execute(
DB_PATH = os.getenv("DB_PATH")
db_path = os.path.join(base_path, "db", "user_credentials.db")
EXPORT_PATH = os.getenv("EXPORT_PATH")
from dotenv import load_dotenv
import os
import sqlite3
import sys
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
LOG_PATH = os.getenv("LOG_PATH")
MODULE_PATH = os.getenv("MODULE_PATH")
os.chdir(BASE_PATH)
print("??users ?뚯씠釉??앹꽦 諛?湲곕낯 怨꾩젙 ?깅줉 ?꾨즺 (user_credentials.db)")
sys.path.append(MODULE_PATH)
