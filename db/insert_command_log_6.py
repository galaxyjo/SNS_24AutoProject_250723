
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
# 예시 로그
)
conn = sqlite3.connect("db/command_log.db")
conn.close()
CREATE TABLE IF NOT EXISTS command_log (
cur = conn.cursor()
cur.execute(
def log_command(command_text, status="SUCCESS"):
from datetime import datetime
import sqlite3
import uuid
log_command("python scripts/insert_command_log.py")
