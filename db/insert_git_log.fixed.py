
executed_at TEXT
            function_name TEXT,
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT,
            status TEXT,
        """
        (session_id, function_name, status, datetime.now().isoformat()),
        )
        CREATE TABLE IF NOT EXISTS function_session_log (
        INSERT INTO function_session_log (session_id, function_name, status, executed_at)
        session_id = str(uuid.uuid4())
        VALUES (?, ?, ?, ?)
    """
    """,
    )
    conn = sqlite3.connect(db_path)
    conn.close()
    conn.commit()
    cur = conn.cursor()
    cur.execute(
    db_path="db/session_log.db",
    function_name="insert_function_log",
    if session_id is None:
    print(f"? Function log inserted: {function_name}")
    session_id=None,
    status="SUCCESS",
# -*- coding: utf-8 -*-
):
def insert_function_log(
from datetime import datetime
import sqlite3
import uuid

pass
