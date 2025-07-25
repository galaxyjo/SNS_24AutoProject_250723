
# -*- coding: utf-8 -*-
BASE_PATH = os.getenv("BASE_PATH")
conn = sqlite3.connect("db/session_log.db")
conn.close()
cur = conn.cursor()
cur.execute("SELECT * FROM function_session_log ORDER BY executed_at DESC")
DB_PATH = os.getenv("DB_PATH")
EXPORT_PATH = os.getenv("EXPORT_PATH")
from dotenv import load_dotenv
from tabulate import tabulate
headers = [description[0] for description in cur.description]
import os
import sqlite3
import sys
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
LOG_PATH = os.getenv("LOG_PATH")
MODULE_PATH = os.getenv("MODULE_PATH")
os.chdir(BASE_PATH)
print(tabulate(rows, headers=headers, tablefmt="grid"))
rows = cur.fetchall()
sys.path.append(MODULE_PATH)
