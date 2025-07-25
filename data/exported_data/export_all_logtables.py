
import sys
import sqlite3
import pandas as pd
import os
from dotenv import load_dotenv
df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
df.to_excel(export_path, index=False)
export_path = f"logs/export_all_{table_name}.xlsx"
table_name = table[0]
# -*- coding: utf-8 -*-
# DB 연결
# Export 디렉토리
# 각 테이블을 엑셀로 저장
# 테이블 목록 조회
BASE_PATH = os.getenv("BASE_PATH")
conn = sqlite3.connect("db/trace_log.db")
conn.close()
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
DB_PATH = os.getenv("DB_PATH")
EXPORT_PATH = os.getenv("EXPORT_PATH")
for table in tables:
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
LOG_PATH = os.getenv("LOG_PATH")
MODULE_PATH = os.getenv("MODULE_PATH")
os.chdir(BASE_PATH)
os.makedirs("logs", exist_ok=True)
sys.path.append(MODULE_PATH)
tables = cursor.fetchall()
