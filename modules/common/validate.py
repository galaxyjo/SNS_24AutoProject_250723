# ✅ modules/common/validate.py (디버깅 완료 버전 – 전체 복붙)

import re
from typing import Optional

# 이메일 정규식 수정 – 도메인에 최소한 하나의 점(.)이 있어야 함
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
URL_REGEX = re.compile(r"^(https?|ftp)://[^\s/$.?#].[^\s]*$", re.IGNORECASE)
ONLY_NUMERIC = re.compile(r"^\d+$")
ONLY_ALPHANUMERIC = re.compile(r"^[a-zA-Z0-9]+$")


def is_email(s: Optional[str]) -> bool:
    return bool(s and EMAIL_REGEX.fullmatch(s.strip()))


def is_url(s: Optional[str]) -> bool:
    return bool(s and URL_REGEX.match(s.strip()))


def is_numeric(s: Optional[str]) -> bool:
    return bool(s and ONLY_NUMERIC.fullmatch(s.strip()))


def is_alphanumeric(s: Optional[str]) -> bool:
    return bool(s and ONLY_ALPHANUMERIC.fullmatch(s.strip()))


def is_blank(s: Optional[str]) -> bool:
    return s is None or s.strip() == ""
