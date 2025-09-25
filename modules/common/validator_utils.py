# modules/common/validator_utils.py
# 🚀 통합 스크립트
# 출처: validator/check_wraps.py, common_3.py
# 기능: 데코레이터 유효성 검사 및 공통 헬퍼

import functools
from typing import Any, Callable


def check_wraps(func: Callable) -> Callable:
    """데코레이터가 원본 함수의 메타데이터를 유지하는지 확인"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


def ensure_not_none(value: Any, name: str = "value") -> Any:
    """None 값이 아닌지 확인"""
    if value is None:
        raise ValueError(f"{name} cannot be None")
    return value


def safe_getattr(obj: Any, attr: str, default: Any = None) -> Any:
    """안전하게 getattr 수행"""
    return getattr(obj, attr, default)


def safe_setattr(obj: Any, attr: str, value: Any) -> None:
    """안전하게 setattr 수행"""
    try:
        setattr(obj, attr, value)
    except Exception as e:
        raise AttributeError(f"Failed to set {attr}: {e}")


def main() -> None:
    """샘플 실행"""
    def sample(x): return x
    wrapped = check_wraps(sample)
    print(wrapped(123))  # ✅ 성공

    print(ensure_not_none("abc"))
    print(safe_getattr({"a": 1}, "get", None))


if __name__ == "__main__":
    main()
