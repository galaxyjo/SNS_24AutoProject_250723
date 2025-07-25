
import sys
import sqlite3
import pandas as pd
import os
import datetime
from dotenv import load_dotenv
+ ".csv"
+ datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
r"C:\BackUp_ehcho_galaxy\logs\export_logtrace_"
# -*- coding: utf-8 -*-
)
    BASE_PATH = os.getenv("BASE_PATH")
    conn = sqlite3.connect(DB_PATH)
    conn.close()
    DB_PATH = os.getenv("DB_PATH")
    DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
    df = pd.read_sql_query("SELECT * FROM log_trace", conn)
    df.to_csv(EXPORT_PATH, index=False, encoding="utf-8")
    EXPORT_PATH = (
EXPORT_PATH = os.getenv("EXPORT_PATH")
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
LOG_PATH = os.getenv("LOG_PATH")
MODULE_PATH = os.getenv("MODULE_PATH")
os.chdir(BASE_PATH)
sys.path.append(MODULE_PATH)
