import os
from typing import Optional


def get_env(key: str, default: str | None = None) -> str | None:
    """환경 변수에서 값을 가져오되, 없으면 기본값 반환"""
    return os.getenv(key, default)


def require_env(key: str) -> str:
    """필수 환경 변수 - 없으면 예외 발생"""
    value = os.getenv(key)
    if value is None:
        raise OSError(f"Missing required environment variable: {key}")
    return value
