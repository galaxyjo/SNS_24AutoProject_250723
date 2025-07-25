
# -*- coding: utf-8 -*-
import sys
import sqlite3
import pandas as pd
import os
from dotenv import load_dotenv
BASE_PATH = os.getenv("BASE_PATH")
conn = sqlite3.connect("db/trace_log.db")
DB_PATH = os.getenv("DB_PATH")
df = pd.read_sql_query("SELECT * FROM log_trace", conn)
df.to_csv("logs/export_logtrace.csv", index=False)
EXPORT_PATH = os.getenv("EXPORT_PATH")
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
LOG_PATH = os.getenv("LOG_PATH")
MODULE_PATH = os.getenv("MODULE_PATH")
os.chdir(BASE_PATH)
print("? 로그 CSV 저장 완료")
sys.path.append(MODULE_PATH)
