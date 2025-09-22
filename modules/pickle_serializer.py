# modules/pickle_serializer.py
"""
Pickle serializer wrapper for Python 3.
Provides simple dumps/loads functions for object serialization.
"""

import pickle
from typing import Any


def dumps(obj: Any) -> bytes:
    """객체를 직렬화하여 bytes로 반환한다."""
    return pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL)


def loads(data: bytes) -> Any:
    """bytes를 역직렬화하여 원본 객체를 반환한다."""
    return pickle.loads(data)
