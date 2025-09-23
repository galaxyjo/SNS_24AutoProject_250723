# -*- coding: utf-8 -*-
"""
export_logtrace_to_csv.py

목적:
- SQLite DB 내 로그 테이블(기본: log_trace)을 CSV로 내보낸다.
- .env 기반 경로/환경 가변 처리, 사전 검증, 함수화/타입힌트, 테스트 가능 구조 준수.
"""

from __future__ import annotations

import os
import sys
import csv
import sqlite3
import datetime as dt
from typing import List, Sequence

from dotenv import load_dotenv


# ── 환경 로드 및 기준 경로 확정 ───────────────────────────────────────────────
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
load_dotenv(dotenv_path=os.path.join(BASE_DIR, ".env"))

BASE_PATH = os.getenv("BASE_PATH", BASE_DIR)
DB_PATH = os.getenv("DB_PATH") or os.path.join(BASE_PATH, "db", "account_log.db")
EXPORT_ROOT = os.getenv("EXPORT_PATH") or os.path.join(BASE_PATH, "logs", "exports")

# 테이블/컬럼 고정값(환경으로 재정의 가능)
LOGTRACE_TABLE = os.getenv("LOGTRACE_TABLE", "log_trace")
# 기본 컬럼 셋: 기존 스키마 기준(가용성 검사 후 교차 사용)
DEFAULT_COLUMNS = [
    "file_name",
    "function_name",
    "desc",
    "GPT_REF",
    "STEP",
    "inserted_at",
]
# LOGTRACE_COLUMNS="col1,col2,..." 형태로 커스터마이즈 가능
_env_cols = os.getenv("LOGTRACE_COLUMNS")
if _env_cols:
    DESIRED_COLUMNS = [c.strip() for c in _env_cols.split(",") if c.strip()]
else:
    DESIRED_COLUMNS = DEFAULT_COLUMNS


# ── 내부 유틸 ────────────────────────────────────────────────────────────────
def _ensure_paths(export_root: str) -> str:
    """
    EXPORT_ROOT 해석: 파일 경로가 들어오면 상위 디렉터리, 디렉터리면 그대로 사용.
    결과적으로 사용될 export 디렉터리 절대경로를 반환.
    """
    # 확장자 있으면 파일 경로로 간주 → 디렉터리만 추출
    if os.path.splitext(export_root)[1]:
        export_dir = os.path.dirname(export_root) or BASE_PATH
    else:
        export_dir = export_root
    os.makedirs(export_dir, exist_ok=True)
    return os.path.abspath(export_dir)


def _validate_inputs(db_path: str) -> None:
    """DB 존재 여부 검증."""
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"DB not found: {db_path}")


def _list_table_columns(conn: sqlite3.Connection, table: str) -> List[str]:
    """PRAGMA로 테이블 컬럼 목록 조회."""
    cur = conn.cursor()
    cur.execute(f"PRAGMA table_info({table});")
    rows = cur.fetchall()
    if not rows:
        raise RuntimeError(f"Table not found or has no columns: {table}")
    return [r[1] for r in rows]  # r[1] == name


def _selectable_columns(available: Sequence[str], desired: Sequence[str]) -> List[str]:
    """
    원하는 컬럼 중 실제 존재하는 컬럼만 반환.
    존재 교집합이 없으면 전체 컬럼(available)로 대체.
    """
    cols = [c for c in desired if c in available]
    return cols if cols else list(available)


# ── 핵심 로직 ────────────────────────────────────────────────────────────────
def export_logtrace_to_csv(
    db_path: str, export_root: str, table: str, desired_columns: Sequence[str]
) -> str:
    """
    로그 테이블을 CSV로 내보낸다.
    반환값: 생성된 CSV의 절대 경로
    """
    _validate_inputs(db_path)
    export_dir = _ensure_paths(export_root)

    # 결과 파일 경로(타임스탬프 포함)
    csv_path = os.path.join(
        export_dir,
        f"export_{table}_{dt.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
    )

    conn = sqlite3.connect(db_path)
    try:
        available_cols = _list_table_columns(conn, table)
        cols = _selectable_columns(available_cols, desired_columns)
        col_list_sql = ", ".join([f'"{c}"' for c in cols])

        cur = conn.cursor()
        cur.execute(f"SELECT {col_list_sql} FROM {table};")
        rows = cur.fetchall()

        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(cols)
            writer.writerows(rows)

    finally:
        conn.close()

    print(f"✅ Export complete → {csv_path}")
    return os.path.abspath(csv_path)


def main() -> None:
    # 작업 디렉터리 및 모듈 경로 세팅
    os.chdir(BASE_PATH)
    if BASE_PATH not in sys.path:
        sys.path.append(BASE_PATH)

    export_logtrace_to_csv(
        db_path=DB_PATH,
        export_root=EXPORT_ROOT,
        table=LOGTRACE_TABLE,
        desired_columns=DESIRED_COLUMNS,
    )


if __name__ == "__main__":
    main()
