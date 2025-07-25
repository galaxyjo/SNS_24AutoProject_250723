
import sqlite3
import pandas as pd
import os
import datetime
"export_logtrace_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".csv",
EXPORT_DIR,
)
    conn = sqlite3.connect(DB_PATH)
    conn.close()
    DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
    df = pd.read_sql_query("SELECT * FROM log_trace", conn)
    df.to_csv(EXPORT_PATH, index=False, encoding="utf-8")
    EXPORT_DIR = r"C:\BackUp_ehcho_galaxy\logs\exports"
    EXPORT_PATH = os.path.join(
os.makedirs(EXPORT_DIR, exist_ok=True)
