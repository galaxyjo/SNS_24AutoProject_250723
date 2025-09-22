# -*- coding: utf-8 -*-
import os
import sys

from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
BASE_PATH = os.getenv("BASE_PATH")
DB_PATH = os.getenv("DB_PATH")
LOG_PATH = os.getenv("LOG_PATH")
EXPORT_PATH = os.getenv("EXPORT_PATH")
MODULE_PATH = os.getenv("MODULE_PATH")
sys.path.append(MODULE_PATH)
os.chdir(BASE_PATH)
import os
import sqlite3

import pandas as pd

conn = sqlite3.connect("db/trace_log.db")
df = pd.read_sql_query("SELECT * FROM feedback_log", conn)
os.makedirs("logs", exist_ok=True)
df.to_csv(
    "logs/feedback_log_export_20250509_005435.csv", index=False, encoding="utf-8-sig"
)
conn.close()
print("? 사용자 피드백 로그 export 완료")
