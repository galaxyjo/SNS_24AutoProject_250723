# modules/common/page_1.py

from typing import List, Any


def paginate(items: List[Any], page_size: int, page_number: int) -> List[Any]:
    """지정된 페이지 크기와 페이지 번호에 따라 리스트를 페이지로 나눔"""
    if page_size <= 0:
        raise ValueError("page_size must be > 0")
    if page_number <= 0:
        raise ValueError("page_number must be > 0")
    start_index = (page_number - 1) * page_size
    end_index = start_index + page_size
    return items[start_index:end_index]


if __name__ == "__main__":
    sample_data = list(range(1, 101))  # 1부터 100까지
    result = paginate(sample_data, page_size=10, page_number=3)
    print("✅ Page 3:", result)
