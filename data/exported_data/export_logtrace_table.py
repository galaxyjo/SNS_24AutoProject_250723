
# -*- coding: utf-8 -*-
import sys
import sqlite3
import pandas as pd
import os
import argparse
from dotenv import load_dotenv
args = parser.parse_args()
BASE_PATH = os.getenv("BASE_PATH")
conn = sqlite3.connect(args.db)
conn.close()
DB_PATH = os.getenv("DB_PATH")
df = pd.read_sql_query(f"SELECT * FROM {args.table}", conn)
df.to_csv(args.out, index=False, encoding="utf-8-sig")
EXPORT_PATH = os.getenv("EXPORT_PATH")
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
LOG_PATH = os.getenv("LOG_PATH")
MODULE_PATH = os.getenv("MODULE_PATH")
os.chdir(BASE_PATH)
os.makedirs(os.path.dirname(args.out), exist_ok=True)
parser = argparse.ArgumentParser()
parser.add_argument("--db", required=True)
parser.add_argument("--out", required=True)
parser.add_argument("--table", required=True)
print(f"? Export 완료 → {args.out}")
sys.path.append(MODULE_PATH)
