# modules/common/sort_helper.py

from typing import List, Callable, Any


def sort_by(
    items: List[Any], key_func: Callable[[Any], Any], reverse: bool = False
) -> List[Any]:
    return sorted(items, key=key_func, reverse=reverse)


def sort_dict_by_key(d: dict, reverse: bool = False) -> dict:
    return dict(sorted(d.items(), key=lambda item: item[0], reverse=reverse))


def sort_dict_by_value(d: dict, reverse: bool = False) -> dict:
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=reverse))
