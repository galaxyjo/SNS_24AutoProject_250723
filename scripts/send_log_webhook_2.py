
    print("✅ 로그 1건 Webhook 전송 성공")
    print(f"❌ 전송 실패: {response.status_code}")
    print(response.json())
# C:\SNS_24AutoProject\scripts\send_log_webhook.py
conn = sqlite3.connect(db_path)
conn.close()
db_path = os.path.join(os.path.dirname(__file__), "..", "db", "trace_log.db")
df = pd.read_sql_query("SELECT * FROM logs ORDER BY timestamp DESC LIMIT 1", conn)
else:
if response.status_code == 200:
import os
import pandas as pd
import requests
import sqlite3
latest_log = df.to_dict(orient="records")[0]
response = requests.post(webhook_url, json=latest_log)
webhook_url = "https://httpbin.org/post"
