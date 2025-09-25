# modules/common/db_helper.py
import os
import sqlite3
from typing import List, Tuple, Any


def get_db_connection(db_path: str) -> sqlite3.Connection:
    """Create and return a new database connection."""
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    return sqlite3.connect(db_path)


def init_logs_table(conn: sqlite3.Connection) -> None:
    """Ensure the logs table exists in the database."""
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            level TEXT,
            message TEXT,
            session_id TEXT
        )
        """
    )
    conn.commit()


def insert_log(
    conn: sqlite3.Connection, timestamp: str, level: str, message: str, session_id: str
) -> None:
    """Insert a single log entry into the logs table."""
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO logs (timestamp, level, message, session_id) VALUES (?, ?, ?, ?)",
        (timestamp, level, message, session_id),
    )
    conn.commit()


def fetch_all_logs(conn: sqlite3.Connection) -> List[Tuple[Any]]:
    """Fetch all logs from the logs table."""
    cur = conn.cursor()
    cur.execute("SELECT * FROM logs ORDER BY timestamp DESC")
    return cur.fetchall()


def init_log_trace_table(conn: sqlite3.Connection) -> None:
    """Ensure the log_trace table exists."""
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS log_trace (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_name TEXT,
            function_name TEXT,
            desc TEXT,
            GPT_REF TEXT,
            STEP TEXT,
            inserted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.commit()


def insert_log_trace(
    conn: sqlite3.Connection,
    file_name: str,
    function_name: str,
    desc: str,
    gpt_ref: str,
    step: str,
) -> None:
    """Insert a single record into the log_trace table."""
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO log_trace (file_name, function_name, desc, GPT_REF, STEP)
        VALUES (?, ?, ?, ?, ?)
        """,
        (file_name, function_name, desc, gpt_ref, step),
    )
    conn.commit()


def fetch_all_log_traces(conn: sqlite3.Connection) -> List[Tuple[Any]]:
    """Fetch all rows from log_trace table."""
    cur = conn.cursor()
    cur.execute("SELECT * FROM log_trace ORDER BY inserted_at DESC")
    return cur.fetchall()
