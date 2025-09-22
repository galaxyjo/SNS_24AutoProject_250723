# -*- coding: utf-8 -*-
import getpass
import os
import platform
import socket
import sqlite3
import sys
from datetime import datetime

from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
BASE_PATH = os.getenv("BASE_PATH")
DB_PATH = os.getenv("DB_PATH")
LOG_PATH = os.getenv("LOG_PATH")
EXPORT_PATH = os.getenv("EXPORT_PATH")
MODULE_PATH = os.getenv("MODULE_PATH")
sys.path.append(MODULE_PATH)
os.chdir(BASE_PATH)

db_path = "db/env_log.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute(
    """
CREATE TABLE IF NOT EXISTS env_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT,
    hostname TEXT,
    os TEXT,
    processor TEXT,
    python_version TEXT,
    created_at TEXT
)
"""
)

env_data = {
    "user": getpass.getuser(),
    "hostname": socket.gethostname(),
    "os": f"{platform.system()} {platform.release()}",
    "processor": platform.processor(),
    "python_version": platform.python_version(),
    "created_at": datetime.now().isoformat(),
}

cur.execute(
    """
    INSERT INTO env_log (user, hostname, os, processor, python_version, created_at)
    VALUES (:user, :hostname, :os, :processor, :python_version, :created_at)
""",
    env_data,
)

conn.commit()
conn.close()
print("???섍꼍 ?뺣낫 濡쒓렇 湲곕줉 ?꾨즺")
