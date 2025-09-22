import datetime
import sqlite3

import pandas as pd

DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
EXPORT_PATH = (
    r"C:\BackUp_ehcho_galaxy\logs\export_logtrace_"
    + datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    + ".csv"
)

conn = sqlite3.connect(DB_PATH)
df = pd.read_sql_query("SELECT * FROM log_trace", conn)
conn.close()

df.to_csv(EXPORT_PATH, index=False, encoding="utf-8")
