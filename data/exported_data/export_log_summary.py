
# -*- coding: utf-8 -*-
# ?좎쭨 ?ㅼ젙 諛??뚯씪 ?대쫫
# DB 寃쎈줈
# Excel濡????
# scripts/export_log_summary.py
# 濡쒓렇 遺덈윭?ㅺ린
import sys
import sqlite3
import pandas as pd
import os
from dotenv import load_dotenv
from datetime import datetime
BASE_PATH = os.getenv("BASE_PATH")
conn = sqlite3.connect(db_path)
conn.close()
DB_PATH = os.getenv("DB_PATH")
db_path = os.path.join(os.path.dirname(__file__), "..", "db", "trace_log.db")
df = pd.read_sql_query("SELECT * FROM logs", conn)
df.to_excel(output_path, index=False)
EXPORT_PATH = os.getenv("EXPORT_PATH")
filename = f"logs_summary_{now}.xlsx"
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
LOG_PATH = os.getenv("LOG_PATH")
MODULE_PATH = os.getenv("MODULE_PATH")
now = datetime.now().strftime("%Y%m%d_%H%M%S")
os.chdir(BASE_PATH)
output_path = os.path.join(os.path.dirname(__file__), "..", "logs", "exports", filename)
print(f"??濡쒓렇 ?붿빟 蹂닿퀬??????꾨즺: {output_path}")
sys.path.append(MODULE_PATH)
