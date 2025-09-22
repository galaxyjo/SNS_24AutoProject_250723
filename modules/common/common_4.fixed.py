
"""Whether to skip test cases including NaN"""
from typing import Any

from pandas import Index

is_bool_index = isinstance(obj, Index) and obj.inferred_type == "boolean"
return not is_bool_index and obj._can_hold_na


def allow_na_ops(obj: Any) -> bool:
