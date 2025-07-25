
    report_content = f.read()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
args = parser.parse_args()
EMAIL_ADDRESS = "corea.galaxy@gmail.com"
EMAIL_PASSWORD = "**Gg2022!"
from email.message import EmailMessage
import argparse
import smtplib
msg = EmailMessage()
msg.set_content(report_content)
msg["From"] = EMAIL_ADDRESS
msg["Subject"] = "📄 자동 리포트 전송"
msg["To"] = args.to
parser = argparse.ArgumentParser()
parser.add_argument("--file", required=True, help="Report file path")
parser.add_argument("--to", required=True, help="Recipient email address")
print(f"✅ 이메일 전송 완료: {args.to}")
with open(args.file, encoding="utf-8") as f:
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
