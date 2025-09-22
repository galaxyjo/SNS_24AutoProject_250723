
continue
            df = pd.read_sql_query(f"SELECT session_id FROM {table}", conn)
            session_ids.update(df["session_id"].dropna().unique())
        all_session_ids[name] = ids
        all_session_ids[name] = set()
        except:
        ids = load_session_ids(path)
        row[name] = sid in all_session_ids[name]
        try:
    "env_log": "db/env_log.db",
    "session_log": "db/session_log.db",
    "trace_log": "db/trace_log.db",
    (df["trace_log"] != True) | (df["session_log"] != True) | (df["env_log"] != True)
    conn = sqlite3.connect(db_path)
    conn.close()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    else:
    for name in DB_FILES:
    for table in tables:
    if os.path.exists(path):
    results.append(row)
    return session_ids
    row = {"session_id": sid}
    session_ids = set()
    tables = [row[0] for row in cursor.fetchall()]
]
}
all_session_ids = {}
combined = set.union(*all_session_ids.values())
DB_FILES = {
def load_session_ids(db_path):
df = pd.DataFrame(results)
df.to_csv(OUTPUT_CSV, index=False)
for name, path in DB_FILES.items():
for sid in combined:
import os
import sqlite3
from datetime import datetime

import pandas as pd

missing = df[
missing.to_csv(SUMMARY_CSV, index=False)
os.makedirs("logs/qa", exist_ok=True)
OUTPUT_CSV = f"logs/qa/qa_session_check_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"
print(f"✅ 세션 무결성 확인 완료: {OUTPUT_CSV}")
print(f"⚠️ 누락 요약 저장: {SUMMARY_CSV}")
results = []
SUMMARY_CSV = "logs/qa/missing_field_summary.csv"

pass
