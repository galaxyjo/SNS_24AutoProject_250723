from types import MappingProxyType, SimpleNamespace
from typing import Any, Iterable, Mapping, Optional, Sequence, Union


def is_mapping(obj: Any) -> bool:
    return isinstance(obj, Mapping)


def is_sequence(obj: Any) -> bool:
    return isinstance(obj, (list, tuple))


def is_string(obj: Any) -> bool:
    return isinstance(obj, (str, bytes))


def to_str(obj: Any) -> str:
    try:
        return obj if isinstance(obj, str) else str(obj)
    except Exception:
        return repr(obj)


__all__ = [
    "Any",
    "Iterable",
    "Mapping",
    "Sequence",
    "Optional",
    "Union",
    "MappingProxyType",
    "SimpleNamespace",
    "is_mapping",
    "is_sequence",
    "is_string",
    "to_str",
]
