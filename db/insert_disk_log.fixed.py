
created_at TEXT
        created_at,
        disk_id TEXT,
        disk_id,
        free_gb REAL,
        hostname TEXT,
        hostname,
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        round(free / (1024**3), 2),
        round(total / (1024**3), 2),
        round(used / (1024**3), 2),
        total_gb REAL,
        used_gb REAL,
    """
    (
    )
    ),
    CREATE TABLE IF NOT EXISTS disk_log (
    INSERT INTO disk_log (disk_id, hostname, total_gb, used_gb, free_gb, created_at)
    VALUES (?, ?, ?, ?, ?, ?)
"""
""",
# -*- coding: utf-8 -*-
# scripts\insert_disk_log.py
)
BASE_PATH = os.getenv("BASE_PATH")
conn = sqlite3.connect("db/disk_log.db")
conn.close()
conn.commit()
created_at = datetime.now().isoformat()
cur = conn.cursor()
cur.execute(
DB_PATH = os.getenv("DB_PATH")
disk_id = str(uuid.uuid4())
EXPORT_PATH = os.getenv("EXPORT_PATH")
from datetime import datetime
from dotenv import load_dotenv
hostname = platform.node()
import os
import platform
import shutil
import sqlite3
import sys
import uuid
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
LOG_PATH = os.getenv("LOG_PATH")
MODULE_PATH = os.getenv("MODULE_PATH")
os.chdir(BASE_PATH)
print("???붿뒪???뺣낫 濡쒓렇 湲곕줉 ?꾨즺")
sys.path.append(MODULE_PATH)
total, used, free = shutil.disk_usage("C:/")

pass
