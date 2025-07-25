
    print("✅ 이메일 전송 성공")
    print(f"❌ 이메일 전송 실패: {e}")
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.login(sender_email, sender_password)
    server.quit()
    server.send_message(msg)
    server.starttls()
# SMTP 전송
# 메시지 구성
# 메일 설정
# 이메일 내용
body = "보고서가 자동 생성되어 첨부됩니다. 전체 로그와 결과를 확인해 주세요."
except Exception as e:
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
msg = MIMEMultipart()
msg.attach(MIMEText(body, "plain"))
msg["From"] = sender_email
msg["Subject"] = subject
msg["To"] = receiver_email
receiver_email = "yourim2kim@gmail.com"
sender_email = "nhm880808@gmail.com"
sender_password = "앱비밀번호"  # Google 계정 앱 비밀번호 입력
smtp_port = 587
smtp_server = "smtp.gmail.com"
subject = "자동화 리포트 보고서"
try:
