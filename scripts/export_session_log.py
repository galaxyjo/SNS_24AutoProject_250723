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
import csv
import sqlite3
from datetime import datetime

conn = sqlite3.connect("db/session_log.db")
cur = conn.cursor()

cur.execute("SELECT * FROM function_session_log ORDER BY executed_at DESC")
rows = cur.fetchall()
headers = [description[0] for description in cur.description]

filename = f"logs/export_session_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
with open(filename, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

print(f"??Export complete: {filename}")
conn.close()
