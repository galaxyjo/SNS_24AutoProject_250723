import os
import platform
import socket
import getpass
import sqlite3
from datetime import datetime

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
print("✅ 환경 정보 로그 기록 완료")
