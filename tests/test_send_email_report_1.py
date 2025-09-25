# tests/test_send_email_report_1.py
import pytest
from scripts import send_email_report_1 as ser

def test_send_report_email_success(monkeypatch):
    sent = {}
    class DummyServer:
        def starttls(self): pass
        def login(self, user, pwd): pass
        def send_message(self, msg): sent.update({"msg": msg})
        def quit(self): pass

    monkeypatch.setattr("smtplib.SMTP", lambda server, port: DummyServer())

    ser.send_report_email("sender@test.com", "password", "receiver@test.com", "subject", "body")
    assert "msg" in sent
