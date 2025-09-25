# modules/common/common_utils.py
# 출처: common_18.py, 20.py, 28.py, 29.py 등 통합
from typing import Any, Union


# ✅ 리스트 요소 가져오기 (출처: common_20.py)
def get_list_element(lst: list, index: int) -> Any:
    if not isinstance(lst, list):
        raise TypeError("lst must be a list")
    if not isinstance(index, int):
        raise TypeError("index must be an integer")
    if index < 0 or index >= len(lst):
        raise IndexError("index out of range")
    return lst[index]


# ✅ 숫자인지 확인 (출처: common_28.py)
def is_numeric(value: Union[str, int, float]) -> bool:
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False


# ✅ 면적 계산 (출처: common_29.py)
def calculate_area(width: float, height: float) -> float:
    return width * height


# ✅ Dict 헬퍼 (출처: common_18.py)
class SimpleDictStore:
    def __init__(self):
        self.data = {}

    def add_entry(self, key: str, value: Any) -> None:
        self.data[key] = value

    def get_entry(self, key: str) -> Any:
        return self.data.get(key)

    def remove_entry(self, key: str) -> None:
        if key in self.data:
            del self.data[key]

    def clear_entries(self) -> None:
        self.data.clear()

    def get_all_entries(self) -> dict:
        return self.data


# ✅ 경로 존재 확인 (출처: audits_1.py → 분리)
import os

def ensure_path_exists(path: str) -> None:
    if not os.path.exists(path):
        raise FileNotFoundError(f"⚠️ 경로 없음: {path}")
