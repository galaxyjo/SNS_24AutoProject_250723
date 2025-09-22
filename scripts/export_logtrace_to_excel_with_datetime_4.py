import datetime
import os
import sqlite3

import pandas as pd

DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
EXPORT_DIR = r"C:\BackUp_ehcho_galaxy\logs\exports"
os.makedirs(EXPORT_DIR, exist_ok=True)

EXPORT_PATH = os.path.join(
    EXPORT_DIR,
    "export_logtrace_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".xlsx",
)

conn = sqlite3.connect(DB_PATH)
df = pd.read_sql_query("SELECT * FROM log_trace", conn)
conn.close()

with pd.ExcelWriter(EXPORT_PATH, engine="xlsxwriter") as writer:
    df.to_excel(writer, sheet_name="log_trace", index=False)
