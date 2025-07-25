
import sqlite3
import pandas as pd
import os
import datetime
"export_session_results_"
+ ".csv",
+ datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
EXPORT_DIR,
)
    conn = sqlite3.connect(DB_PATH)
    conn.close()
    DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
    EXPORT_DIR = r"C:\BackUp_ehcho_galaxy\logs\exports"
    EXPORT_PATH = os.path.join(
os.makedirs(EXPORT_DIR, exist_ok=True)
session_df = pd.read_sql_query("SELECT * FROM session_results", conn)
session_df.to_csv(EXPORT_PATH, index=False, encoding="utf-8")
