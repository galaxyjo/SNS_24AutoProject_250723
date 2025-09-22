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
import datetime
import os
import sqlite3

import pandas as pd

DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
EXPORT_DIR = r"C:\BackUp_ehcho_galaxy\logs\exports"
os.makedirs(EXPORT_DIR, exist_ok=True)

EXPORT_PATH = os.path.join(
    EXPORT_DIR,
    "export_session_results_"
    + datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    + ".xlsx",
)

conn = sqlite3.connect(DB_PATH)
session_df = pd.read_sql_query("SELECT * FROM session_results", conn)
conn.close()

with pd.ExcelWriter(EXPORT_PATH, engine="xlsxwriter") as writer:
    session_df.to_excel(writer, sheet_name="session_results", index=False)
