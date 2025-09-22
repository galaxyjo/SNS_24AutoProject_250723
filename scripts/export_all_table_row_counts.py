# -*- coding: utf-8 -*-
"""
Export table row counts to a timestamped CSV.

고정 규칙:
- .env의 BASE_PATH, DB_PATH, EXPORT_PATH 우선 사용 (없으면 BASE_DIR 기준 fallback)
- 경로/파일 사전 검증, 명확한 완료/경고 메시지
- 함수화 + 타입힌트 + 테스트 가능 구조
"""

from __future__ import annotations

import os
import sys
import csv
import sqlite3
import datetime as dt
from typing import List, Tuple

import pandas as pd  # noqa: F401  # (향후 확장 호환성 유지용)
from dotenv import load_dotenv


# --- 환경 로드 & 기본 경로 결정 ---
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
load_dotenv(dotenv_path=os.path.join(BASE_DIR, ".env"))

BASE_PATH = os.getenv("BASE_PATH", BASE_DIR)
DB_PATH = os.getenv("DB_PATH")
EXPORT_ROOT = os.getenv("EXPORT_PATH")  # 디렉터리 또는 파일 경로로 사용 가능


def _ensure_paths() -> Tuple[str, str]:
    """
    환경값을 해석하여 DB 경로와 Export 디렉터리를 확정한다.
    - DB_PATH 미지정: <BASE_PATH>/db/account_log.db
    - EXPORT_ROOT 미지정: <BASE_PATH>/logs/exports
    - EXPORT_ROOT가 파일 경로로 주어지면 그 상위 디렉터리를 export 디렉터리로 사용
    """
    db_path = DB_PATH or os.path.join(BASE_PATH, "db", "account_log.db")

    export_root = EXPORT_ROOT or os.path.join(BASE_PATH, "logs", "exports")
    # 파일 경로가 들어왔을 경우 디렉터리만 취득
    if os.path.splitext(export_root)[1]:
        export_dir = os.path.dirname(export_root)
        if not export_dir:
            export_dir = BASE_PATH
    else:
        export_dir = export_root

    return db_path, export_dir


def _validate_inputs(db_path: str, export_dir: str) -> None:
    """필수 경로/파일 존재 여부 검증."""
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"DB not found: {db_path}")
    os.makedirs(export_dir, exist_ok=True)


def _list_tables(conn: sqlite3.Connection) -> List[str]:
    """sqlite_master에서 테이블 목록을 조회한다."""
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [r[0] for r in cur.fetchall()]
    if not tables:
        raise RuntimeError("No tables found in DB")
    return tables


def export_table_row_counts(db_path: str, export_dir: str) -> str:
    """
    DB 내 모든 테이블의 row count를 CSV로 내보낸다.

    Returns:
        생성된 CSV의 절대경로
    """
    _validate_inputs(db_path, export_dir)

    csv_path = os.path.join(
        export_dir,
        f"export_table_row_counts_{dt.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
    )

    conn = sqlite3.connect(db_path)
    try:
        tables = _list_tables(conn)
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["table_name", "row_count"])
            cur = conn.cursor()
            for t in tables:
                try:
                    cur.execute(f"SELECT COUNT(*) FROM {t}")
                    count = int(cur.fetchone()[0])
                    writer.writerow([t, count])
                except Exception as e:
                    # 특정 테이블 실패 시 경고 출력 후 계속 진행
                    print(f"⚠️ Failed to count table {t}: {e}")
    finally:
        conn.close()

    print(f"✅ Export complete → {csv_path}")
    return os.path.abspath(csv_path)


def main() -> None:
    db_path, export_dir = _ensure_paths()
    # 작업 디렉토리 및 모듈 경로 정리
    os.chdir(BASE_PATH)
    if BASE_PATH not in sys.path:
        sys.path.append(BASE_PATH)
    export_table_row_counts(db_path, export_dir)


if __name__ == "__main__":
    main()
