
import sqlite3
import pandas as pd
git_commits_df.to_excel(writer, sheet_name="git_commits", index=False)
hook_logs_df.to_excel(writer, sheet_name="hook_logs", index=False)
log_trace_df.to_excel(writer, sheet_name="log_trace", index=False)
conn = sqlite3.connect(DB_PATH)
conn.close()
DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
EXPORT_PATH = r"C:\BackUp_ehcho_galaxy\logs\export_all_logtables_20250501.xlsx"
git_commits_df = pd.read_sql_query("SELECT * FROM git_commits", conn)
hook_logs_df = pd.read_sql_query("SELECT * FROM hook_logs", conn)
log_trace_df = pd.read_sql_query("SELECT * FROM log_trace", conn)
with pd.ExcelWriter(EXPORT_PATH, engine="xlsxwriter") as writer:
