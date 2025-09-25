# modules/common/hook_status_logger.py

import os
import sqlite3
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

BASE_PATH = os.getenv("BASE_PATH", os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
DB_PATH = os.getenv("DB_PATH", os.path.join(BASE_PATH, "db", "hook_status.db"))

def init_db(db_path: str = DB_PATH) -> None:
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS hook_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            status TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            reason TEXT
        );
    """)
    conn.commit()
    conn.close()

def log_status(status: str, reason: str = None, db_path: str = DB_PATH) -> None:
    if not os.path.exists(db_path):
        init_db(db_path)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO hook_logs (status, timestamp, reason)
        VALUES (?, ?, ?);
    """, (status, datetime.utcnow().isoformat(), reason))
    conn.commit()
    conn.close()
