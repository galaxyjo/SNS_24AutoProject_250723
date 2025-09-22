
executed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id TEXT,
        status TEXT,
    (session_id, status),
    )
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
    f"""
    INSERT INTO {TABLE_NAME} (session_id, status)
    VALUES (?, ?)
"""
""",
)
conn = sqlite3.connect(DB_PATH)
conn.close()
conn.commit()
cur = conn.cursor()
cur.execute(
DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
import datetime
import sqlite3
session_id = f'session_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}'
status = "completed"
TABLE_NAME = "session_results"

pass
