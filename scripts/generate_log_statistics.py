# scripts/generate_log_statistics.py

import os
import sqlite3
from datetime import datetime
from typing import List, Dict, Optional

import pandas as pd
from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.getenv("DB_PATH", "db/trace_log.db")
EXPORT_DIR = os.getenv("EXPORT_DIR", "logs/stats")
os.makedirs(EXPORT_DIR, exist_ok=True)

LOG_TABLES = [
    "command_log",
    "disk_log",
    "env_log",
    "function_session_log",
    "git_log",
    "network_log",
]


def fetch_log_statistics(db_path: str = DB_PATH, tables: Optional[List[str]] = None) -> List[Dict]:
    if tables is None:
        tables = LOG_TABLES

    if not os.path.exists(db_path):
        raise FileNotFoundError(f"❌ DB 파일이 존재하지 않습니다: {db_path}")

    stats_all = []
    conn = sqlite3.connect(db_path)

    try:
        for table in tables:
            try:
                df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
                now = datetime.now().strftime("%Y%m%d_%H%M%S")
                stats = {
                    "table": table,
                    "row_count": len(df),
                    "columns": list(df.columns),
                    "last_updated": df.iloc[-1]["executed_at"] if "executed_at" in df.columns else "N/A",
                }

                stat_df = pd.DataFrame([stats])
                export_path = os.path.join(EXPORT_DIR, f"{table}_stats_{now}.csv")
                stat_df.to_csv(export_path, index=False, encoding="utf-8-sig")

                print(f"✅ {table} 통계 요약 완료 → {export_path}")
                stats_all.append(stats)

            except Exception as e:
                print(f"⚠️ {table} 처리 실패: {e}")
    finally:
        conn.close()

    return stats_all


def main():
    fetch_log_statistics()


if __name__ == "__main__":
    main()
