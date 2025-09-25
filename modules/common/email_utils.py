# modules/common/email_utils.py
# 출처: common_19.py 리팩토링

import re


def extract_emails(text: str) -> list[str]:
    """텍스트에서 이메일 주소 추출"""
    if not isinstance(text, str):
        return []
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, text)


def is_valid_email(email: str) -> bool:
    """이메일 형식이 유효한지 검사"""
    if not isinstance(email, str):
        return False
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def mask_email(email: str) -> str:
    """이메일을 마스킹 처리 (ex: j****e@example.com)"""
    if not is_valid_email(email):
        return email
    local, domain = email.split("@")
    if len(local) <= 2:
        return f"{local}@{domain}"
    masked_local = local[0] + "*" * (len(local) - 2) + local[-1]
    return f"{masked_local}@{domain}"
