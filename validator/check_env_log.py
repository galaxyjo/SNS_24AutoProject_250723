
    print("?좑툘 No environment log data found.")
    print(df.to_markdown(index=False))
# -*- coding: utf-8 -*-
BASE_PATH = os.getenv("BASE_PATH")
conn = sqlite3.connect("db/env_log.db")
conn.close()
DB_PATH = os.getenv("DB_PATH")
df = pd.read_sql_query("SELECT * FROM env_log ORDER BY created_at DESC", conn)
else:
EXPORT_PATH = os.getenv("EXPORT_PATH")
from dotenv import load_dotenv
if df.empty:
import os
import pandas as pd
import sqlite3
import sys
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
LOG_PATH = os.getenv("LOG_PATH")
MODULE_PATH = os.getenv("MODULE_PATH")
os.chdir(BASE_PATH)
sys.path.append(MODULE_PATH)
