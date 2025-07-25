
# -*- coding: utf-8 -*-
import sys
import sqlite3
import pandas as pd
import os
from dotenv import load_dotenv
from datetime import datetime
BASE_PATH = os.getenv("BASE_PATH")
conn = sqlite3.connect("db/network_log.db")
conn.close()
DB_PATH = os.getenv("DB_PATH")
df = pd.read_sql_query("SELECT * FROM network_log", conn)
df.to_csv(filename, index=False)
EXPORT_PATH = os.getenv("EXPORT_PATH")
filename = f"logs/export_network_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
LOG_PATH = os.getenv("LOG_PATH")
MODULE_PATH = os.getenv("MODULE_PATH")
os.chdir(BASE_PATH)
print(f"??Export complete: {filename}")
sys.path.append(MODULE_PATH)
