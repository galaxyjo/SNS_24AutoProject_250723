
import sqlite3
import pandas as pd
import datetime
+ ".xlsx"
+ datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
df.to_excel(writer, sheet_name="log_trace", index=False)
r"C:\BackUp_ehcho_galaxy\logs\export_logtrace_"
)
    conn = sqlite3.connect(DB_PATH)
    conn.close()
    DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
    df = pd.read_sql_query("SELECT * FROM log_trace", conn)
    EXPORT_PATH = (
with pd.ExcelWriter(EXPORT_PATH, engine="xlsxwriter") as writer:
