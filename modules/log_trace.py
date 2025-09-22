# modules/log_trace.py
from __future__ import annotations
import sqlite3
from datetime import datetime
from typing import List, Dict, Any, Optional


def get_run_at_timestamp() -> str:
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")


def init_log_db(
    conn: sqlite3.Connection | None = None, db_path: Optional[str] = None
) -> sqlite3.Connection:
    con = conn or sqlite3.connect(db_path or ":memory:", check_same_thread=False)

    con.execute(
        """
        CREATE TABLE IF NOT EXISTS session_log (
            session_id TEXT PRIMARY KEY,
            run_at TEXT,
            status TEXT
        )
    """
    )

    con.execute(
        """
        CREATE TABLE IF NOT EXISTS account_run_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ts TEXT NOT NULL,
            account TEXT NOT NULL,
            session_id TEXT,
            status TEXT NOT NULL,
            message TEXT
        )
    """
    )
    con.commit()
    return con


def get_logger():
    import logging

    logger = logging.getLogger("SNSLogger")
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger


def log_account_run(
    account: str,
    success: bool = True,
    session_id: Optional[str] = None,
    message: str = "",
    run_at: Optional[str] = None,
    conn: Optional[sqlite3.Connection] = None,
    db_path: Optional[str] = None,
) -> Optional[bool]:
    con = conn or init_log_db(db_path=db_path)
    ts = run_at or datetime.utcnow().isoformat(timespec="seconds") + "Z"
    status = "SUCCESS" if success else "FAIL"
    con.execute(
        "INSERT INTO account_run_log (ts, account, session_id, status, message) VALUES (?,?,?,?,?)",
        (ts, account, session_id, status, message),
    )
    con.commit()
    return True


# ✅ 순서 수정 완료
def insert_session_log(
    sess_id: str,
    run_at: str,
    status: str,
    conn: Optional[sqlite3.Connection] = None,
    db_path: Optional[str] = None,
) -> Optional[bool]:
    con = conn or init_log_db(db_path=db_path)
    con.execute(
        "INSERT INTO session_log (session_id, run_at, status) VALUES (?, ?, ?)",
        (sess_id, run_at, status),
    )
    con.commit()
    return True


# ✅ 컬럼명 수정 완료
def insert_account_run_log(
    session_id: str,
    account: str,
    success: bool,
    run_at: str,
    conn: Optional[sqlite3.Connection] = None,
    db_path: Optional[str] = None,
) -> Optional[bool]:
    con = conn or init_log_db(db_path=db_path)
    status = "SUCCESS" if success else "FAIL"
    con.execute(
        "INSERT INTO account_run_log (ts, account, session_id, status, message) VALUES (?, ?, ?, ?, ?)",
        (run_at, account, session_id, status, ""),
    )
    con.commit()
    return True


def get_all_logs(
    conn: Optional[sqlite3.Connection] = None,
    db_path: Optional[str] = None,
    limit: int = 100,
) -> List[Dict[str, Any]]:
    con = conn or init_log_db(db_path=db_path)
    rows = con.execute(
        "SELECT id, ts, account, session_id, status, message FROM account_run_log ORDER BY id DESC LIMIT ?",
        (limit,),
    ).fetchall()
    return [
        {
            "id": r[0],
            "ts": r[1],
            "account": r[2],
            "session_id": r[3],
            "status": r[4],
            "message": r[5],
        }
        for r in rows
    ]
