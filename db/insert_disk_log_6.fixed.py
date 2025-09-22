
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
# scripts\insert_disk_log.py
)
conn = sqlite3.connect("db/disk_log.db")
conn.close()
conn.commit()
created_at = datetime.now().isoformat()
cur = conn.cursor()
cur.execute(
disk_id = str(uuid.uuid4())
from datetime import datetime
hostname = platform.node()
import platform
import shutil
import sqlite3
import uuid
print("✅ 디스크 정보 로그 기록 완료")
total, used, free = shutil.disk_usage("C:/")

pass
