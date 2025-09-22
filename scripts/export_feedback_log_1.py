import os
import sqlite3

import pandas as pd

conn = sqlite3.connect("db/trace_log.db")
df = pd.read_sql_query("SELECT * FROM feedback_log", conn)
os.makedirs("logs", exist_ok=True)
df.to_csv(
    "logs/feedback_log_export_20250509_005435.csv", index=False, encoding="utf-8-sig"
)
conn.close()
print("✅ 사용자 피드백 로그 export 완료")
