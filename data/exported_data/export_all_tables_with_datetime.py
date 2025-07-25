
        df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
        df.to_excel(writer, sheet_name=table, index=False)
    "export_all_tables_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".xlsx",
    EXPORT_DIR,
    for table in tables["name"]:
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
from dotenv import load_dotenv
import datetime
import os
import pandas as pd
import sqlite3
import sys
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
LOG_PATH = os.getenv("LOG_PATH")
MODULE_PATH = os.getenv("MODULE_PATH")
os.chdir(BASE_PATH)
os.makedirs(EXPORT_DIR, exist_ok=True)
sys.path.append(MODULE_PATH)
tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", conn)
with pd.ExcelWriter(EXPORT_PATH, engine="xlsxwriter") as writer:
