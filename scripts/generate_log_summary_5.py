
        conn = sqlite3.connect(db_path)
        conn.close()
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        df.to_csv(output_path, index=False, encoding="utf-8-sig")
        output_path = f"logs/summary/{name}_log_summary_{now}.csv"
        print(f"✅ {name}_log 요약 완료 → {output_path}")
        print(f"❌ {name}_log 요약 실패: {e}")
    "command": ("db/command_log.db", "command_log"),
    "disk": ("db/disk_log.db", "disk_log"),
    "env": ("db/env_log.db", "env_log"),
    "function": ("db/session_log.db", "function_session_log"),
    "git": ("db/trace_log.db", "git_log"),
    "network": ("db/network_log.db", "network_log"),
    except Exception as e:
    try:
# 각 로그 테이블별 CSV 저장
# 로그 테이블과 대응되는 DB 경로 설정
# 출력 경로 생성
}
db_map = {
for name, (db_path, table_name) in db_map.items():
from datetime import datetime
import os
import pandas as pd
import sqlite3
now = datetime.now().strftime("%Y%m%d_%H%M%S")
os.makedirs("logs/summary", exist_ok=True)
