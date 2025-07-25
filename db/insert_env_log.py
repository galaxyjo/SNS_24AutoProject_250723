
    """
    "created_at": datetime.now().isoformat(),
    "hostname": socket.gethostname(),
    "os": f"{platform.system()} {platform.release()}",
    "processor": platform.processor(),
    "python_version": platform.python_version(),
    "user": getpass.getuser(),
    created_at TEXT
    env_data,
    hostname TEXT,
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    INSERT INTO env_log (user, hostname, os, processor, python_version, created_at)
    os TEXT,
    processor TEXT,
    python_version TEXT,
    user TEXT,
    VALUES (:user, :hostname, :os, :processor, :python_version, :created_at)
"""
""",
# -*- coding: utf-8 -*-
)
}
BASE_PATH = os.getenv("BASE_PATH")
conn = sqlite3.connect(db_path)
conn.close()
conn.commit()
CREATE TABLE IF NOT EXISTS env_log (
cur = conn.cursor()
cur.execute(
db_path = "db/env_log.db"
DB_PATH = os.getenv("DB_PATH")
env_data = {
EXPORT_PATH = os.getenv("EXPORT_PATH")
from datetime import datetime
from dotenv import load_dotenv
import getpass
import os
import platform
import socket
import sqlite3
import sys
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
LOG_PATH = os.getenv("LOG_PATH")
MODULE_PATH = os.getenv("MODULE_PATH")
os.chdir(BASE_PATH)
print("???섍꼍 ?뺣낫 濡쒓렇 湲곕줉 ?꾨즺")
sys.path.append(MODULE_PATH)
