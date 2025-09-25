# scripts/auto_git_webhook.py
# =============================
# 출처: auto_git_webhook.py
import os
import subprocess
import requests

def send_git_webhook():
    output = (
        subprocess.check_output(
            ["git", "log", "-1", "--pretty=format:%H%n%an%n%ae%n%ad%n%s"],
            cwd=os.path.join(os.path.dirname(__file__), ".."),
        )
        .decode("utf-8")
        .split("\n")
    )
    git_log = {
        "commit_hash": output[0],
        "author_name": output[1],
        "author_email": output[2],
        "date": output[3],
        "message": output[4],
    }
    webhook_url = "https://httpbin.org/post"
    res = requests.post(webhook_url, json=git_log)
    if res.status_code == 200:
        print("✅ 최근 Git 커밋 Webhook 전송 성공")
    else:
        print(f"❌ 전송 실패: {res.status_code}")
        print(res.json())

if __name__ == "__main__":
    send_git_webhook()
