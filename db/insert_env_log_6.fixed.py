
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
)
}
conn = sqlite3.connect(db_path)
conn.close()
conn.commit()
CREATE TABLE IF NOT EXISTS env_log (
cur = conn.cursor()
cur.execute(
db_path = "db/env_log.db"
env_data = {
from datetime import datetime
import getpass
import platform
import socket
import sqlite3
print("✅ 환경 정보 로그 기록 완료")

pass
