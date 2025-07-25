
        """
        (str(uuid.uuid4()), command_text, status, datetime.now().isoformat()),
        INSERT INTO command_log (command_id, command_text, status, executed_at)
        VALUES (?, ?, ?, ?)
    """
    """,
    )
    command_id TEXT,
    command_text TEXT,
    conn.commit()
    cur.execute(
    executed_at TEXT
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    status TEXT,
"""
# -*- coding: utf-8 -*-
# ?덉떆 濡쒓렇
)
BASE_PATH = os.getenv("BASE_PATH")
conn = sqlite3.connect("db/command_log.db")
conn.close()
CREATE TABLE IF NOT EXISTS command_log (
cur = conn.cursor()
cur.execute(
DB_PATH = os.getenv("DB_PATH")
def log_command(command_text, status="SUCCESS"):
EXPORT_PATH = os.getenv("EXPORT_PATH")
from datetime import datetime
from dotenv import load_dotenv
import os
import sqlite3
import sys
import uuid
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
log_command("python scripts/insert_command_log.py")
LOG_PATH = os.getenv("LOG_PATH")
MODULE_PATH = os.getenv("MODULE_PATH")
os.chdir(BASE_PATH)
sys.path.append(MODULE_PATH)
