# scripts/send_summary_email_1.py (정상화/디버깅 완료)
import argparse
import smtplib
from email.message import EmailMessage
import os

def send_summary_email(file_path: str, to_email: str):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"⚠️ Report file not found: {file_path}")

    EMAIL_ADDRESS = "corea.galaxy@gmail.com"
    EMAIL_PASSWORD = "**Gg2022!"

    with open(file_path, encoding="utf-8") as f:
        report_content = f.read()

    msg = EmailMessage()
    msg.set_content(report_content)
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email
    msg["Subject"] = "📄 자동 리포트 전송"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    print(f"✅ 이메일 전송 완료: {to_email}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="Report file path")
    parser.add_argument("--to", required=True, help="Recipient email address")
    args = parser.parse_args()

    send_summary_email(args.file, args.to)


if __name__ == "__main__":
    main()
