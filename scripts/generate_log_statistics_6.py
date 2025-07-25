
                df.iloc[-1]["executed_at"] if "executed_at" in df.columns else "N/A"
            "columns": list(df.columns),
            "last_updated": (
            "row_count": len(df),
            ),
            f"logs/stats/{table}_stats_{now}.csv", index=False, encoding="utf-8-sig"
        )
        }
        df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
        print(f"✅ {table} 통계 요약 완료")
        print(f"❌ {table} 처리 실패: {e}")
        stat_df = pd.DataFrame([stats])
        stat_df.to_csv(
        stats = {
    "command_log",
    "disk_log",
    "env_log",
    "function_session_log",
    "git_log",
    "network_log",
    except Exception as e:
    try:
# 파일명: scripts/generate_log_statistics.py
]
conn = sqlite3.connect("db/trace_log.db")
conn.close()
cursor = conn.cursor()
for table in log_tables:
from datetime import datetime
import os
import pandas as pd
import sqlite3
log_tables = [
now = datetime.now().strftime("%Y%m%d_%H%M%S")
os.makedirs("logs/stats", exist_ok=True)
