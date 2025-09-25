# tests/test_email_utils.py

from modules.common.email_utils import extract_emails, is_valid_email, mask_email


def test_extract_emails():
    text = "Contact us: test@example.com and help@domain.co"
    result = extract_emails(text)
    assert "test@example.com" in result
    assert "help@domain.co" in result


def test_is_valid_email():
    assert is_valid_email("valid@email.com") is True
    assert is_valid_email("not-an-email") is False
    assert is_valid_email("") is False
    assert is_valid_email(None) is False


def test_mask_email():
    assert mask_email("johndoe@example.com") == "j*****e@example.com"
    assert mask_email("ab@example.com") == "ab@example.com"  # 2자 이하면 그대로
    assert mask_email("invalid") == "invalid"  # invalid는 그대로
