
("pre-commit", "fail", str(e)),
        ("pre-commit", "success", result.stdout.strip()),
        executed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        f"""
        hook_type TEXT,
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        INSERT INTO {TABLE_NAME} (hook_type, status, message)
        message TEXT,
        status TEXT,
        VALUES (?, ?, ?)
    """,
    )
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
    cur.execute(
    f"""
    result = subprocess.run(["git", "status"], capture_output=True, text=True)
"""
# -*- coding: utf-8 -*-
)
conn = sqlite3.connect(DB_PATH)
conn.close()
conn.commit()
cur = conn.cursor()
cur.execute(
DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
except Exception as e:
import sqlite3
import subprocess

TABLE_NAME = "hook_logs"
try:
