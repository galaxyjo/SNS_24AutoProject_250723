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
import os

# scripts/export_log_summary.py
import sqlite3
from datetime import datetime

import pandas as pd

# DB 寃쎈줈
db_path = os.path.join(os.path.dirname(__file__), "..", "db", "trace_log.db")
conn = sqlite3.connect(db_path)

# 濡쒓렇 遺덈윭?ㅺ린
df = pd.read_sql_query("SELECT * FROM logs", conn)
conn.close()

# ?좎쭨 ?ㅼ젙 諛??뚯씪 ?대쫫
now = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"logs_summary_{now}.xlsx"
output_path = os.path.join(os.path.dirname(__file__), "..", "logs", "exports", filename)

# Excel濡????
df.to_excel(output_path, index=False)
print(f"??濡쒓렇 ?붿빟 蹂닿퀬??????꾨즺: {output_path}")
