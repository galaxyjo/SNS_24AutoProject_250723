
(r["file_name"], r["function_name"], r["desc"], r["GPT_REF"], r["STEP"])
        desc TEXT,
        file_name TEXT,
        for r in reader
        function_name TEXT,
        GPT_REF TEXT,
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        inserted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        STEP TEXT,
    )
    ]
    CREATE TABLE IF NOT EXISTS {table_name} (
    f"""
    INSERT INTO {table_name} (file_name, function_name, desc, GPT_REF, STEP)
    reader = csv.DictReader(f)
    rows = [
    rows,
    VALUES (?, ?, ?, ?, ?)
"""
""",
# -*- coding: utf-8 -*-
# CSV → DB 삽입
# DB 연결 및 테이블 생성
# 경로 설정
)
base_dir = r"C:\BackUp_ehcho_galaxy"
conn = sqlite3.connect(db_path)
conn.close()
conn.commit()
csv_path = os.path.join(base_dir, "logs", "insert_log_2025-05-01.csv")
cur = conn.cursor()
cur.execute(
cur.executemany(
db_path = os.path.join(base_dir, "logs", "trace_log.db")
import csv
import os
import sqlite3
table_name = "log_trace"
with open(csv_path, encoding="utf-8") as f:
