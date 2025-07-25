
import sqlite3
import pandas as pd
import datetime
+ ".csv"
+ datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
r"C:\BackUp_ehcho_galaxy\logs\export_logtrace_"
)
    conn = sqlite3.connect(DB_PATH)
    conn.close()
    DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
    df = pd.read_sql_query("SELECT * FROM log_trace", conn)
    df.to_csv(EXPORT_PATH, index=False, encoding="utf-8")
    EXPORT_PATH = (
