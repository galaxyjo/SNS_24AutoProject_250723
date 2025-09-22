# -*- coding: utf-8 -*-
import os
import sys

from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
BASE_PATH = os.getenv("BASE_PATH")
DB_PATH = os.getenv("DB_PATH")
LOG_PATH = os.getenv("LOG_PATH")
EXPORT_PATH = os.getenv("EXPORT_PATH")
MODULE_PATH = os.getenv("MODULE_PATH")
sys.path.append(MODULE_PATH)
os.chdir(BASE_PATH)
import sqlite3

import pandas as pd

DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
EXPORT_PATH = r"C:\BackUp_ehcho_galaxy\logs\export_all_logtables_20250501.xlsx"

conn = sqlite3.connect(DB_PATH)
log_trace_df = pd.read_sql_query("SELECT * FROM log_trace", conn)
git_commits_df = pd.read_sql_query("SELECT * FROM git_commits", conn)
hook_logs_df = pd.read_sql_query("SELECT * FROM hook_logs", conn)
conn.close()

with pd.ExcelWriter(EXPORT_PATH, engine="xlsxwriter") as writer:
    log_trace_df.to_excel(writer, sheet_name="log_trace", index=False)
    git_commits_df.to_excel(writer, sheet_name="git_commits", index=False)
    hook_logs_df.to_excel(writer, sheet_name="hook_logs", index=False)
