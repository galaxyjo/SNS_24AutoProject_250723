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
    + ".csv",
)

conn = sqlite3.connect(DB_PATH)
session_df = pd.read_sql_query("SELECT * FROM session_results", conn)
conn.close()

session_df.to_csv(EXPORT_PATH, index=False, encoding="utf-8")
