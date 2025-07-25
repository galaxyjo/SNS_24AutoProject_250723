
import sys
import sqlite3
import pandas as pd
import os
import datetime
from dotenv import load_dotenv
"export_logtrace_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".csv",
EXPORT_DIR,
# -*- coding: utf-8 -*-
)
    BASE_PATH = os.getenv("BASE_PATH")
    conn = sqlite3.connect(DB_PATH)
    conn.close()
    DB_PATH = os.getenv("DB_PATH")
    DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
    df = pd.read_sql_query("SELECT * FROM log_trace", conn)
    df.to_csv(EXPORT_PATH, index=False, encoding="utf-8")
    EXPORT_DIR = r"C:\BackUp_ehcho_galaxy\logs\exports"
    EXPORT_PATH = os.getenv("EXPORT_PATH")
    EXPORT_PATH = os.path.join(
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
LOG_PATH = os.getenv("LOG_PATH")
MODULE_PATH = os.getenv("MODULE_PATH")
os.chdir(BASE_PATH)
os.makedirs(EXPORT_DIR, exist_ok=True)
sys.path.append(MODULE_PATH)
