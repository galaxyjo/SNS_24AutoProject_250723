# modules/common/retry_util.py

import time
from typing import Any

from collections.abc import Callable


def retry(func: Callable, retries: int = 3, delay: float = 0.5) -> Any:
    """
    Retry the given function up to `retries` times with a delay between attempts.
    """
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            if attempt == retries - 1:
                raise
            time.sleep(delay)
