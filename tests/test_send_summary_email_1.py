# tests/test_send_summary_email_1.py
import pytest
import tempfile
from scripts import send_summary_email_1 as sse
from unittest.mock import patch, MagicMock

@pytest.fixture
def temp_report_file():
    with tempfile.NamedTemporaryFile("w+", encoding="utf-8", delete=False) as f:
        f.write("테스트 리포트 내용")
        f.flush()
        yield f.name

def test_send_summary_email_success(temp_report_file):
    with patch("smtplib.SMTP_SSL") as mock_smtp:
        instance = mock_smtp.return_value.__enter__.return_value
        instance.login.return_value = None
        instance.send_message.return_value = None
        sse.send_summary_email(temp_report_file, "test@example.com")
        instance.login.assert_called_once()
        instance.send_message.assert_called_once()
