# modules/common/str_enum.py
# UTF-8 (no BOM), LF
from __future__ import annotations

from enum import Enum, auto
from typing import Any, Iterable, List, Optional, Type, TypeVar

__all__ = ["StrEnum"]

E = TypeVar("E", bound="StrEnum")


class StrEnum(str, Enum):
    """
    Lightweight backport/variant of Python 3.11+ enum.StrEnum.

    Features:
      - string values
      - auto() -> lowercased name
      - from_any(...) tolerant parser (name/value, case-insensitive optional)
      - helpers: names(), values(), has_name(), has_value()
      - __str__ returns the underlying value
    """

    # auto() support: map name -> value (lowercase by default)
    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: List[str]) -> str:  # type: ignore[override]
        return name.lower()

    def __new__(cls: Type[E], value: str) -> E:  # type: ignore[override]
        if not isinstance(value, str):
            raise TypeError(
                f"{cls.__name__} requires string values, got {type(value)!r}"
            )
        obj = str.__new__(cls, value)
        obj._value_ = value  # type: ignore[attr-defined]
        return obj  # type: ignore[return-value]

    def __str__(self) -> str:
        return self.value

    # ---------- Introspection ----------
    @classmethod
    def names(cls: Type[E]) -> List[str]:
        return [m.name for m in cls]

    @classmethod
    def values(cls: Type[E]) -> List[str]:
        return [m.value for m in cls]

    @classmethod
    def has_name(cls: Type[E], name: str, *, casefold: bool = False) -> bool:
        if not isinstance(name, str):
            return False
        if not casefold:
            return name in cls.__members__
        n = name.casefold()
        return any(m.name.casefold() == n for m in cls)

    @classmethod
    def has_value(cls: Type[E], value: str, *, casefold: bool = False) -> bool:
        if not isinstance(value, str):
            return False
        if not casefold:
            return value in cls._value2member_map_  # type: ignore[attr-defined]
        v = value.casefold()
        return any(m.value.casefold() == v for m in cls)

    # ---------- Parsing ----------
    @classmethod
    def from_any(
        cls: Type[E],
        v: Any,
        default: Optional[E] = None,
        *,
        casefold: bool = True,
    ) -> E:
        """
        Parse from:
          - same enum instance -> returned
          - string name or value (case-insensitive by default)
          - raw value mapped by Enum (exact match fallback)
        On failure: returns `default` if provided, else raises ValueError.
        """
        # already enum
        if isinstance(v, cls):
            return v

        # None handling
        if v is None:
            if default is not None:
                return default
            raise ValueError(f"None is not a valid {cls.__name__}")

        # string: try value or name
        if isinstance(v, str):
            if casefold:
                needle = v.casefold()
                for m in cls:
                    if m.value.casefold() == needle or m.name.casefold() == needle:
                        return m
            else:
                if v in cls._value2member_map_:  # type: ignore[attr-defined]
                    return cls(v)  # type: ignore[call-arg]
                mem = cls.__members__.get(v)
                if mem is not None:
                    return mem  # type: ignore[return-value]

        # exact enum construction as a last resort
        try:
            return cls(v)  # type: ignore[call-arg]
        except Exception:
            if default is not None:
                return default
            raise ValueError(f"{v!r} is not a valid {cls.__name__}")

    # ---------- Serialization ----------
    def to_json(self) -> str:
        """
        JSON-friendly representation: the underlying string value.
        """
        return self.value
