# modules/common/memoize_util.py

from functools import wraps
from typing import Callable, Dict, Tuple, Any


def memoize(func: Callable) -> Callable:
    cache: Dict[Tuple[Any, ...], Any] = {}

    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return wrapper
