
        print("✅ Webhook 전송 성공")
        print(f"❌ Webhook 실패: {response.status_code} - {response.text}")
    "report_path": r"C:\SNS_24AutoProject\logs\reports\function_report_20250515_135038.xlsx"
    "text": "✅ 자동 보고서가 생성되었습니다.",
    else:
    headers = {'Content-Type': 'application/json'}
    if response.status_code == 200:
    response = requests.post(WEBHOOK_URL, data=json.dumps(payload), headers=headers)
    send_webhook()
# -*- coding: utf-8 -*-
# Webhook URL (예시: Discord / Zapier / Slack)
# 보낼 데이터 (간단한 예시)
}
def send_webhook():
if __name__ == "__main__":
import json
import requests
payload = {
WEBHOOK_URL = "https://your-webhook-url.com"
