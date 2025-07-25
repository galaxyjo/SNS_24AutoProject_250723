
import sys
import sqlite3
import pandas as pd
import os
from dotenv import load_dotenv
"logs/feedback_log_export_20250509_005435.csv", index = False, encoding = "utf-8-sig"
# -*- coding: utf-8 -*-
)
    BASE_PATH = os.getenv("BASE_PATH")
    conn = sqlite3.connect("db/trace_log.db")
    conn.close()
    DB_PATH = os.getenv("DB_PATH")
    df = pd.read_sql_query("SELECT * FROM feedback_log", conn)
    df.to_csv(
EXPORT_PATH = os.getenv("EXPORT_PATH")
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
LOG_PATH = os.getenv("LOG_PATH")
MODULE_PATH = os.getenv("MODULE_PATH")
os.chdir(BASE_PATH)
os.makedirs("logs", exist_ok=True)
print("? 사용자 피드백 로그 export 완료")
sys.path.append(MODULE_PATH)
