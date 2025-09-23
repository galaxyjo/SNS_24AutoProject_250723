# -*- coding: utf-8 -*-
"""
init_check_create_logtable.py

목적:
- SQLite DB 내 로그 테이블(logs) 존재 여부를 확인하고, 없으면 생성한다.
- session_results 등 불필요한 로직은 포함하지 않는다.
- .env 기반 경로 처리, 사전 검증, 함수화/타입힌트, 테스트 가능 구조 준수.
"""

from __future__ import annotations

import os
import sys
import sqlite3
from typing import Optional

from dotenv import load_dotenv

# ── 환경 로드 및 기준 경로 확정 ───────────────────────────────────────────────
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
load_dotenv(dotenv_path=os.path.join(BASE_DIR, ".env"))

BASE_PATH = os.getenv("BASE_PATH", BASE_DIR)
DB_PATH = os.getenv("DB_PATH") or os.path.join(BASE_PATH, "db", "trace_log.db")
LOG_TABLE = os.getenv("LOG_TABLE", "logs")


# ── 핵심 로직 ────────────────────────────────────────────────────────────────
def init_check_create_logtable(db_path: str = DB_PATH, table: str = LOG_TABLE) -> bool:
    """
    로그 테이블 존재 확인 후, 없으면 생성한다.

    Args:
        db_path: SQLite DB 파일 경로
        table: 생성/확인할 테이블명 (기본: logs)

    Returns:
        bool: True → 테이블이 존재하거나 새로 생성됨 / False → 실패
    """
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    conn: Optional[sqlite3.Connection] = None
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {table} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                level TEXT,
                message TEXT,
                session_id TEXT
            );
            """
        )
        conn.commit()
        print(f"✅ Table check complete → {table} in {db_path}")
        return True
    except Exception as e:
        print(f"⚠️ Failed to create/check table {table}: {e}")
        return False
    finally:
        if conn:
            conn.close()


def main() -> None:
    os.chdir(BASE_PATH)
    if BASE_PATH not in sys.path:
        sys.path.append(BASE_PATH)

    init_check_create_logtable()


if __name__ == "__main__":
    main()
