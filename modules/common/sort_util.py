# modules/common/sort_util.py

from typing import Any, Callable, List, Dict


def sort_list(
    items: List[Any], key: Callable = None, reverse: bool = False
) -> List[Any]:
    try:
        return sorted(items, key=key, reverse=reverse)
    except Exception:
        return []


def sort_dict_by_key(d: Dict[Any, Any], reverse: bool = False) -> Dict[Any, Any]:
    try:
        return dict(sorted(d.items(), key=lambda item: item[0], reverse=reverse))
    except Exception:
        return {}


def sort_dict_by_value(d: Dict[Any, Any], reverse: bool = False) -> Dict[Any, Any]:
    try:
        return dict(sorted(d.items(), key=lambda item: item[1], reverse=reverse))
    except Exception:
        return {}
