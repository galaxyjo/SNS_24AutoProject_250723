# scripts/send_email_report_1.py (디버깅/정상화 버전)
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_report_email(sender_email: str, sender_password: str, receiver_email: str, subject: str, body: str):
    try:
        msg = MIMEMultipart()
        msg.attach(MIMEText(body, "plain"))
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject

        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()

        print("✅ 이메일 전송 성공")
    except Exception as e:
        print(f"❌ 이메일 전송 실패: {e}")
        raise e


def main():
    sender_email = "nhm880808@gmail.com"
    sender_password = "**Gg2022!"
    receiver_email = "yourim2kim@gmail.com"
    subject = "자동화 리포트 보고서"
    body = "보고서가 자동 생성되어 첨부됩니다. 전체 로그와 결과를 확인해 주세요."

    send_report_email(sender_email, sender_password, receiver_email, subject, body)


if __name__ == "__main__":
    main()
