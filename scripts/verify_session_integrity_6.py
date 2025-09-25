# scripts/verify_session_integrity_6.py
import os
import sqlite3
from datetime import datetime

import pandas as pd

DB_FILES = {
    "env_log": "db/env_log.db",
    "session_log": "db/session_log.db",
    "trace_log": "db/trace_log.db",
}

OUTPUT_DIR = os.path.join("logs", "qa")
os.makedirs(OUTPUT_DIR, exist_ok=True)
OUTPUT_CSV = os.path.join(OUTPUT_DIR, f"qa_session_check_{datetime.now().strftime('%Y%m%d_%H%M')}.csv")
SUMMARY_CSV = os.path.join(OUTPUT_DIR, "missing_field_summary.csv")


def load_session_ids(db_path):
    if not os.path.exists(db_path):
        return set()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [row[0] for row in cursor.fetchall()]
    session_ids = set()
    for table in tables:
        try:
            df = pd.read_sql_query(f"SELECT session_id FROM {table}", conn)
            session_ids.update(df["session_id"].dropna().unique())
        except Exception:
            continue
    conn.close()
    return session_ids


def main():
    all_session_ids = {}
    for name, path in DB_FILES.items():
        all_session_ids[name] = load_session_ids(path)

    combined_ids = set.union(*[ids for ids in all_session_ids.values() if ids])
    results = []

    for name, ids in all_session_ids.items():
        row = {}
        for sid in combined_ids:
            row[sid] = sid in ids
        results.append(row)

    df = pd.DataFrame(results)
    df.to_csv(OUTPUT_CSV, index=False)

    # 누락 체크
    missing = df[(df != True).any(axis=1)]
    if not missing.empty:
        missing.to_csv(SUMMARY_CSV, index=False)
        print(f"⚠️ 누락 요약 저장: {SUMMARY_CSV}")

    print(f"✅ 세션 무결성 확인 완료: {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
