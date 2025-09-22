import sqlite3
import uuid
from datetime import datetime


def insert_function_log(
    session_id=None,
    function_name="insert_function_log",
    status="SUCCESS",
    db_path="db/session_log.db",
    gpt_prompt=None,
    gpt_response=None,
):
    if session_id is None:
        session_id = str(uuid.uuid4())

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS function_session_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT,
            function_name TEXT,
            status TEXT,
            executed_at TEXT,
            gpt_prompt TEXT,
            gpt_response TEXT
        )
    """
    )

    cur.execute(
        """
        INSERT INTO function_session_log (
            session_id, function_name, status, executed_at, gpt_prompt, gpt_response
        ) VALUES (?, ?, ?, ?, ?, ?)
    """,
        (
            session_id,
            function_name,
            status,
            datetime.now().isoformat(),
            gpt_prompt,
            gpt_response,
        ),
    )

    conn.commit()
    conn.close()

    print(f"? Function log inserted: {function_name} / Session: {session_id}")
