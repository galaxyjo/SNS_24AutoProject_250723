
# DB 경로
# Excel로 저장
# scripts/export_log_summary.py
# 날짜 설정 및 파일 이름
# 로그 불러오기
import sqlite3
import pandas as pd
import os
from datetime import datetime
conn = sqlite3.connect(db_path)
conn.close()
db_path = os.path.join(os.path.dirname(__file__), "..", "db", "trace_log.db")
df = pd.read_sql_query("SELECT * FROM logs", conn)
df.to_excel(output_path, index=False)
filename = f"logs_summary_{now}.xlsx"
now = datetime.now().strftime("%Y%m%d_%H%M%S")
output_path = os.path.join(os.path.dirname(__file__), "..", "logs", "exports", filename)
print(f"✅ 로그 요약 보고서 저장 완료: {output_path}")
