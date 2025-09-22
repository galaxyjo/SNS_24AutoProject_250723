import os
from typing import Optional


def get_env_variable(key: str, default: Optional[str] = None) -> Optional[str]:
    """
    Get an environment variable. Return default if not found.
    """
    return os.environ.get(key, default)


def is_env_true(key: str) -> bool:
    """
    Return True if environment variable is set to '1', 'true', or 'yes' (case-insensitive).
    """
    value = os.environ.get(key, "").lower()
    return value in {"1", "true", "yes"}


def set_env_variable(key: str, value: str) -> None:
    """
    Set an environment variable.
    """
    os.environ[key] = value
