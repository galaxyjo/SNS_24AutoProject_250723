# -*- coding: utf-8 -*-
"""
export_log_summary_csv_with_datetime.py

목적:
- SQLite DB의 모든 테이블에 대해 row count 요약을 CSV로 내보낸다(타임스탬프 포함).
- .env 기반 경로/환경 처리, 사전 검증, 함수화/타입힌트, 테스트 가능 구조 준수.
"""

from __future__ import annotations

import csv
import os
import sys
import sqlite3
import datetime as dt
from typing import List, Tuple

from dotenv import load_dotenv


# ── 환경 로드 및 기준 경로 확정 ───────────────────────────────────────────────
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
load_dotenv(dotenv_path=os.path.join(BASE_DIR, ".env"))

BASE_PATH = os.getenv("BASE_PATH", BASE_DIR)
DB_PATH = os.getenv("DB_PATH")
EXPORT_ROOT = os.getenv("EXPORT_PATH")  # 디렉터리 또는 파일 경로


def _resolve_paths() -> Tuple[str, str]:
    """
    환경값 해석:
    - DB_PATH 미지정: <BASE_PATH>/db/account_log.db
    - EXPORT_ROOT 미지정: <BASE_PATH>/logs/exports
    - EXPORT_ROOT가 파일 경로면 상위 디렉터리를 export 디렉터리로 사용
    """
    db_path = DB_PATH or os.path.join(BASE_PATH, "db", "account_log.db")

    export_root = EXPORT_ROOT or os.path.join(BASE_PATH, "logs", "exports")
    if os.path.splitext(export_root)[1]:  # 확장자 있으면 파일 경로로 간주
        export_dir = os.path.dirname(export_root) or BASE_PATH
    else:
        export_dir = export_root

    return db_path, os.path.abspath(export_dir)


def _validate(db_path: str, export_dir: str) -> None:
    """필수 경로/파일 존재 여부 검증."""
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"DB not found: {db_path}")
    os.makedirs(export_dir, exist_ok=True)


def _list_tables(conn: sqlite3.Connection) -> List[str]:
    """sqlite_master에서 테이블 목록 조회."""
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [r[0] for r in cur.fetchall()]
    if not tables:
        raise RuntimeError("No tables found in DB")
    return tables


def export_log_summary_csv_with_datetime(db_path: str, export_dir: str) -> str:
    """
    DB 내 모든 테이블의 row count 요약을 CSV로 내보낸다.
    Returns:
        생성된 CSV의 절대 경로
    """
    _validate(db_path, export_dir)

    csv_path = os.path.join(
        export_dir,
        f"log_summary_{dt.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
    )

    conn = sqlite3.connect(db_path)
    try:
        tables = _list_tables(conn)
        cur = conn.cursor()

        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["table_name", "row_count"])
            for t in tables:
                try:
                    cur.execute(f"SELECT COUNT(*) FROM {t}")
                    cnt = int(cur.fetchone()[0])
                    writer.writerow([t, cnt])
                except Exception as e:
                    # 특정 테이블에서 오류가 발생해도 전체 작업은 계속 진행
                    print(f"⚠️ Failed to count table {t}: {e}")

    finally:
        conn.close()

    print(f"✅ Export complete → {csv_path}")
    return os.path.abspath(csv_path)


def main() -> None:
    db_path, export_dir = _resolve_paths()

    # 작업 디렉토리 및 모듈 경로 정리
    os.chdir(BASE_PATH)
    if BASE_PATH not in sys.path:
        sys.path.append(BASE_PATH)

    export_log_summary_csv_with_datetime(db_path, export_dir)


if __name__ == "__main__":
    main()
