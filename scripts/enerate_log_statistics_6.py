
        df = pd.read_sql(f"SELECT * FROM {table}", conn)
        print("\n")
        print(df.describe(include="all"))
        print(f"❌ {table} 통계 요약 실패: {e}")
        print(f"📊 {table} 총 행 수: {len(df)}")
    "command_log",
    "disk_log",
    "env_log",
    "function_session_log",
    "git_log",
    "network_log",
    except Exception as e:
    try:
]
conn = sqlite3.connect(db_path)
conn.close()
db_path = "db/trace_log.db"
for table in log_tables:
import pandas as pd
import sqlite3
log_tables = [
