# scripts/export_log_summary.py
import os
import sqlite3
from datetime import datetime

import pandas as pd

# DB 경로
db_path = os.path.join(os.path.dirname(__file__), "..", "db", "trace_log.db")
conn = sqlite3.connect(db_path)

# 로그 불러오기
df = pd.read_sql_query("SELECT * FROM logs", conn)
conn.close()

# 날짜 설정 및 파일 이름
now = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"logs_summary_{now}.xlsx"
output_path = os.path.join(os.path.dirname(__file__), "..", "logs", "exports", filename)

# Excel로 저장
df.to_excel(output_path, index=False)
print(f"✅ 로그 요약 보고서 저장 완료: {output_path}")
