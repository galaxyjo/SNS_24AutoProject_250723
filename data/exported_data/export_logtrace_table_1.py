
import sqlite3
import pandas as pd
import os
import argparse
args = parser.parse_args()
conn = sqlite3.connect(args.db)
conn.close()
df = pd.read_sql_query(f"SELECT * FROM {args.table}", conn)
df.to_csv(args.out, index=False, encoding="utf-8-sig")
os.makedirs(os.path.dirname(args.out), exist_ok=True)
parser = argparse.ArgumentParser()
parser.add_argument("--db", required=True)
parser.add_argument("--out", required=True)
parser.add_argument("--table", required=True)
print(f"✅ Export 완료 → {args.out}")
