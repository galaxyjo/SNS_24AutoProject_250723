# core/logger.py
# -*- coding: utf-8 -*-
"""
- init_db()             : 테이블이 없으면 생성
- insert_session_log()  : 새 세션 INSERT 또는 기존 세션 UPDATE
"""

from __future__ import annotations

import sqlite3
import uuid
from datetime import datetime
from pathlib import Path
from typing import Optional, Tuple

# DB 파일 경로 설정
_BASE_DIR = Path(__file__).resolve().parents[1]  # core/ 기준 상위 경로
_DB_PATH = _BASE_DIR / "logs" / "session.db"
_DB_PATH.parent.mkdir(parents=True, exist_ok=True)

# 연결 객체 생성


def _get_conn_cur() -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    conn = sqlite3.connect(_DB_PATH)
    return conn, conn.cursor()


# 테이블 생성


def init_db() -> None:
    conn, c = _get_conn_cur()
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS session_log (
            id TEXT PRIMARY KEY,
            start_ts TEXT,
            end_ts TEXT,
            status TEXT,
            message TEXT
        )
    """
    )
    conn.commit()
    conn.close()


# 세션 로그 기록


def insert_session_log(
    session_id: Optional[str] = None,
    status: str = "",
    message: str = "",
    timestamp: Optional[str] = None,
) -> str:
    ts = timestamp or datetime.utcnow().isoformat()
    conn, c = _get_conn_cur()

    if session_id is None:
        session_id = str(uuid.uuid4())
        c.execute(
            """
            INSERT INTO session_log (id, start_ts, status, message)
            VALUES (?, ?, ?, ?)
        """,
            (session_id, ts, status, message),
        )
    else:
        c.execute(
            """
            UPDATE session_log
            SET end_ts = ?, status = ?, message = ?
            WHERE id = ?
        """,
            (ts, status, message, session_id),
        )

    conn.commit()
    conn.close()
    return session_id


# 테스트용 실행
if __name__ == "__main__":
    init_db()
    sid = insert_session_log(status="INIT", message="✅ 테스트 로그 생성됨")
    print(f"✔️ 테스트 세션 ID: {sid}")
