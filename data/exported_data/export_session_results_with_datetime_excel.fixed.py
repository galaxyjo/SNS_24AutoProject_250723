
import datetime
import os
import sqlite3
import sys

import pandas as pd
from dotenv import load_dotenv

"export_session_results_"
+ ".xlsx",
+ datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
EXPORT_DIR,
session_df.to_excel(writer, sheet_name="session_results", index=False)
# -*- coding: utf-8 -*-
)
    BASE_PATH = os.getenv("BASE_PATH")
    conn = sqlite3.connect(DB_PATH)
    conn.close()
    DB_PATH = os.getenv("DB_PATH")
    DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
    EXPORT_DIR = r"C:\BackUp_ehcho_galaxy\logs\exports"
    EXPORT_PATH = os.getenv("EXPORT_PATH")
    EXPORT_PATH = os.path.join(
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
LOG_PATH = os.getenv("LOG_PATH")
MODULE_PATH = os.getenv("MODULE_PATH")
os.chdir(BASE_PATH)
os.makedirs(EXPORT_DIR, exist_ok=True)
session_df = pd.read_sql_query("SELECT * FROM session_results", conn)
sys.path.append(MODULE_PATH)
with pd.ExcelWriter(EXPORT_PATH, engine="xlsxwriter") as writer:
