
import sqlite3
import pandas as pd
import os
df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
df.to_excel(export_path, index=False)
export_path = f"logs/export_all_{table_name}.xlsx"
table_name = table[0]
# DB 연결
# Export 디렉토리
# 각 테이블을 엑셀로 저장
# 테이블 목록 조회
conn = sqlite3.connect("db/trace_log.db")
conn.close()
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
for table in tables:
os.makedirs("logs", exist_ok=True)
tables = cursor.fetchall()
