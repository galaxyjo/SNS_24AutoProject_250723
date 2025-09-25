# -*- coding: utf-8 -*-
"""
export_session_results_with_datetime_excel.py

목적:
- SQLite DB의 세션 결과 테이블을 타임스탬프가 포함된 Excel 파일로 내보낸다.
- .env 기반 경로/환경 처리, 사전 검증, 함수화/타입힌트, 테스트 가능 구조 준수.
"""

from __future__ import annotations

import os
import sys
import sqlite3
import datetime as dt
from typing import Optional

import pandas as pd
from dotenv import load_dotenv

# ── 환경 로드 및 기준 경로 확정 ───────────────────────────────────────────────
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
load_dotenv(dotenv_path=os.path.join(BASE_DIR, ".env"))

BASE_PATH = os.getenv("BASE_PATH", BASE_DIR)
DB_PATH = os.getenv("DB_PATH") or os.path.join(BASE_PATH, "db", "account_log.db")
EXPORT_ROOT = os.getenv("EXPORT_PATH") or os.path.join(BASE_PATH, "logs", "exports")
SESSION_TABLE = os.getenv("SESSION_TABLE", "session_results")  # 기본 테이블명

# ── 내부 유틸 ────────────────────────────────────────────────────────────────
def _ensure_export_dir(root: str) -> str:
    """
    EXPORT_ROOT 해석:
    - 파일 경로가 들어오면 상위 디렉터리를 export 디렉터리로 사용
    - 디렉터리 경로가 들어오면 그대로 사용
    """
    if os.path.splitext(root)[1]:
        export_dir = os.path.dirname(root) or BASE_PATH
    else:
        export_dir = root
    os.makedirs(export_dir, exist_ok=True)
    return os.path.abspath(export_dir)


def _validate_inputs(db_path: str, export_dir: str, table: str) -> None:
    """DB, 디렉터리, 테이블명 등 사전 검증."""
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"DB not found: {db_path}")
    os.makedirs(export_dir, exist_ok=True)
    if not table or not isinstance(table, str):
        raise ValueError("SESSION_TABLE must be a non-empty string.")


def _pick_excel_engine() -> str:
    """xlsxwriter 우선, 미설치 시 openpyxl로 대체."""
    try:
        __import__("xlsxwriter")
        return "xlsxwriter"
    except Exception:
        return "openpyxl"


# ── 핵심 로직 ────────────────────────────────────────────────────────────────
def export_session_results_with_datetime_excel(
    db_path: str,
    export_root: str,
    table: str = "session_results",
    where_clause: Optional[str] = None,
) -> str:
    """
    세션 결과 테이블을 Excel로 내보낸다(파일명에 타임스탬프 포함).

    Args:
        db_path: SQLite DB 절대경로
        export_root: 내보내기 루트(파일 또는 디렉터리)
        table: 내보낼 테이블명 (기본: session_results)
        where_clause: 선택적 필터(SQL WHERE 절만 전달, 예: "WHERE success=1")

    Returns:
        생성된 Excel 파일의 절대경로
    """
    export_dir = _ensure_export_dir(export_root)
    _validate_inputs(db_path, export_dir, table)

    excel_path = os.path.join(
        export_dir,
        f"export_{table}_{dt.datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
    )

    query = f'SELECT * FROM "{table}"'
    if where_clause:
        # where_clause는 "WHERE ..." 형태만 허용
        wc = where_clause.strip()
        if not wc.lower().startswith("where"):
            raise ValueError('where_clause must start with "WHERE"')
        query = f'{query} {wc}'

    conn = sqlite3.connect(db_path)
    try:
        df = pd.read_sql_query(query, conn)
    finally:
        conn.close()

    engine = _pick_excel_engine()
    with pd.ExcelWriter(excel_path, engine=engine) as writer:
        # 시트명은 31자 제한
        sheet_name = (table or "session_results")[:31]
        df.to_excel(writer, sheet_name=sheet_name, index=False)

    print(f"✅ Export complete → {excel_path}")
    return os.path.abspath(excel_path)


def main() -> None:
    # 작업 디렉터리 및 모듈 경로 세팅
    os.chdir(BASE_PATH)
    if BASE_PATH not in sys.path:
        sys.path.append(BASE_PATH)

    export_session_results_with_datetime_excel(
        db_path=DB_PATH,
        export_root=EXPORT_ROOT,
        table=SESSION_TABLE,
        where_clause=None,  # 예: 'WHERE success=1'
    )


if __name__ == "__main__":
    main()
