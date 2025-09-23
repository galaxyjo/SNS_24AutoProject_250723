# modules/common/common_19.py

import re


def extract_emails(text):
    if not isinstance(text, str):
        return []
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, text)


def is_valid_email(email):
    if not isinstance(email, str):
        return False
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def mask_email(email):
    if not is_valid_email(email):
        return email
    local, domain = email.split("@")
    masked_local = local[0] + "*" * (len(local) - 2) + local[-1] if len(local) > 2 else local
    return f"{masked_local}@{domain}"
