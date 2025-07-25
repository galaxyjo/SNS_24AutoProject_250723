
        executed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id TEXT,
        status TEXT,
    (session_id, status),
    )
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
    f"""
    INSERT INTO {TABLE_NAME} (session_id, status)
    VALUES (?, ?)
"""
""",
# -*- coding: utf-8 -*-
)
BASE_PATH = os.getenv("BASE_PATH")
conn = sqlite3.connect(DB_PATH)
conn.close()
conn.commit()
cur = conn.cursor()
cur.execute(
DB_PATH = os.getenv("DB_PATH")
DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
EXPORT_PATH = os.getenv("EXPORT_PATH")
from dotenv import load_dotenv
import datetime
import os
import sqlite3
import sys
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
LOG_PATH = os.getenv("LOG_PATH")
MODULE_PATH = os.getenv("MODULE_PATH")
os.chdir(BASE_PATH)
session_id = f'session_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}'
status = "completed"
sys.path.append(MODULE_PATH)
TABLE_NAME = "session_results"
