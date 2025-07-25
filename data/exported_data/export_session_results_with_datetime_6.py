
import sqlite3
import pandas as pd
import datetime
+ ".xlsx"
+ datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
r"C:\BackUp_ehcho_galaxy\logs\export_session_results_"
session_df.to_excel(writer, sheet_name="session_results", index=False)
)
    conn = sqlite3.connect(DB_PATH)
    conn.close()
    DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
    EXPORT_PATH = (
session_df = pd.read_sql_query("SELECT * FROM session_results", conn)
with pd.ExcelWriter(EXPORT_PATH, engine="xlsxwriter") as writer:
