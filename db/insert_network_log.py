
    """
    (network_id, hostname, ip_address, timestamp),
    created_at TEXT
    hostname TEXT,
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip_address TEXT,
    network_id TEXT,
"""
""",
# -*- coding: utf-8 -*-
)
BASE_PATH = os.getenv("BASE_PATH")
conn = sqlite3.connect("db/network_log.db")
conn.close()
conn.commit()
CREATE TABLE IF NOT EXISTS network_log (
cur = conn.cursor()
cur.execute(
DB_PATH = os.getenv("DB_PATH")
EXPORT_PATH = os.getenv("EXPORT_PATH")
from datetime import datetime
from dotenv import load_dotenv
hostname = socket.gethostname()
import os
import socket
import sqlite3
import sys
import uuid
INSERT INTO network_log (network_id, hostname, ip_address, created_at)
ip_address = socket.gethostbyname(hostname)
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
LOG_PATH = os.getenv("LOG_PATH")
MODULE_PATH = os.getenv("MODULE_PATH")
network_id = str(uuid.uuid4())
os.chdir(BASE_PATH)
print("???ㅽ듃?뚰겕 ?뺣낫 濡쒓렇 湲곕줉 ?꾨즺")
sys.path.append(MODULE_PATH)
timestamp = datetime.now().isoformat()
VALUES (?, ?, ?, ?)
