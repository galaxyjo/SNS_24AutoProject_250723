
            datetime.now().isoformat(),
            executed_at TEXT,
            function_name TEXT,
            function_name,
            gpt_prompt TEXT,
            gpt_prompt,
            gpt_response TEXT
            gpt_response,
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT,
            session_id,
            session_id, function_name, status, executed_at, gpt_prompt, gpt_response
            status TEXT,
            status,
        """
        (
        )
        ) VALUES (?, ?, ?, ?, ?, ?)
        ),
        CREATE TABLE IF NOT EXISTS function_session_log (
        INSERT INTO function_session_log (
        session_id = str(uuid.uuid4())
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
    gpt_prompt=None,
    gpt_response=None,
    if session_id is None:
    print(f"? Function log inserted: {function_name} / Session: {session_id}")
    session_id=None,
    status="SUCCESS",
# -*- coding: utf-8 -*-
):
def insert_function_log(
from datetime import datetime
import sqlite3
import uuid
