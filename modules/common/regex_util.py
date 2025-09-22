import re
from typing import Optional


def match_pattern(pattern: str, text: str) -> Optional[re.Match]:
    if not pattern or not text:
        return None
    try:
        return re.match(pattern, text)
    except re.error:
        return None


def search_pattern(pattern: str, text: str) -> Optional[re.Match]:
    if not pattern or not text:
        return None
    try:
        return re.search(pattern, text)
    except re.error:
        return None


def is_valid_pattern(pattern: str) -> bool:
    try:
        re.compile(pattern)
        return True
    except re.error:
        return False
