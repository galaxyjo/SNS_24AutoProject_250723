from typing import Union


def is_numeric(value: Union[str, int, float]) -> bool:
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False
