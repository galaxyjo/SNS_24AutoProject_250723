import os
import sqlite3

import pandas as pd

# DB 연결
conn = sqlite3.connect("db/trace_log.db")
cursor = conn.cursor()

# 테이블 목록 조회
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()

# Export 디렉토리
os.makedirs("logs", exist_ok=True)

# 각 테이블을 엑셀로 저장
for table in tables:
    table_name = table[0]
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    export_path = f"logs/export_all_{table_name}.xlsx"
    df.to_excel(export_path, index=False)

conn.close()
