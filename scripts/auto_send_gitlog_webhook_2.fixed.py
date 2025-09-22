
["git", "log", "-1", "--pretty=format:%H%n%an%n%ae%n%ad%n%s"],
        cwd = os.path.join(os.path.dirname(__file__), ".."),
    "author_email": output[2],
    "author_name": output[1],
    "commit_hash": output[0],
    "date": output[3],
    "message": output[4],
    )
    .decode("utf-8")
    .split("\n")
    print("✅ 최근 Git 커밋 Webhook 전송 성공")
    print(f"❌ 전송 실패: {res.status_code}")
    print(res.json())
    subprocess.check_output(
# C:\SNS_24AutoProject\scripts\auto_send_gitlog_webhook.py
)
}
else:
git_log = {
if res.status_code == 200:
import os
import subprocess

import requests

output = (
res = requests.post(webhook_url, json=git_log)
webhook_url = "https://httpbin.org/post"

pass
