
        count = df.iloc[0, 0]
        df = pd.read_sql_query(f"SELECT COUNT(*) FROM {table}", conn)
        f.write(f"{table}, {count}\n")
    + ".csv"
    + datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    f.write("Table Name, Row Count\n")
    for table in tables["name"]:
    r"C:\BackUp_ehcho_galaxy\logs\export_all_tables_"
# -*- coding: utf-8 -*-
)
BASE_PATH = os.getenv("BASE_PATH")
conn = sqlite3.connect(DB_PATH)
conn.close()
DB_PATH = os.getenv("DB_PATH")
DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
EXPORT_PATH = (
EXPORT_PATH = os.getenv("EXPORT_PATH")
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
sys.path.append(MODULE_PATH)
tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", conn)
with open(EXPORT_PATH, "w", newline="", encoding="utf-8") as f:
