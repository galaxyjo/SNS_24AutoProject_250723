# scripts/send_log_webhook_2.py (정상화/디버깅 버전)
import os
import sqlite3
import pandas as pd
import requests


DB_PATH = os.path.join(os.path.dirname(__file__), "..", "db", "trace_log.db")
WEBHOOK_URL = "https://httpbin.org/post"


def send_latest_log(db_path: str = DB_PATH, webhook_url: str = WEBHOOK_URL):
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"⚠️ DB 파일 없음: {db_path}")

    conn = sqlite3.connect(db_path)
    try:
        df = pd.read_sql_query(
            "SELECT * FROM logs ORDER BY timestamp DESC LIMIT 1", conn
        )
        if df.empty:
            print("⚠️ 전송할 로그가 없습니다")
            return None
        latest_log = df.to_dict(orient="records")[0]
    finally:
        conn.close()

    response = requests.post(webhook_url, json=latest_log)
    if response.status_code == 200:
        print("✅ 로그 1건 Webhook 전송 성공")
    else:
        print(f"❌ 전송 실패: {response.status_code}")
        print(response.json())
    return response


def main():
    send_latest_log()


if __name__ == "__main__":
    main()
