
    """
    (network_id, hostname, ip_address, timestamp),
    created_at TEXT
    hostname TEXT,
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip_address TEXT,
    network_id TEXT,
"""
""",
)
conn = sqlite3.connect("db/network_log.db")
conn.close()
conn.commit()
CREATE TABLE IF NOT EXISTS network_log (
cur = conn.cursor()
cur.execute(
from datetime import datetime
hostname = socket.gethostname()
import socket
import sqlite3
import uuid
INSERT INTO network_log (network_id, hostname, ip_address, created_at)
ip_address = socket.gethostbyname(hostname)
network_id = str(uuid.uuid4())
print("✅ 네트워크 정보 로그 기록 완료")
timestamp = datetime.now().isoformat()
VALUES (?, ?, ?, ?)
