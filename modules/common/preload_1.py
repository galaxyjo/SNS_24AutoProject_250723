import os
import json
from typing import Any, Optional


def get_base_path() -> str:
    return os.environ.get("BASE_PATH", os.getcwd())


def get_preload_path(filename: str = "preload.json") -> str:
    return os.path.join(get_base_path(), filename)


def load_preload_data(path: Optional[str] = None) -> dict[str, Any]:
    if path is None:
        path = get_preload_path()

    if not os.path.exists(path):
        raise FileNotFoundError(f"⚠️ preload 파일 없음: {path}")

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    print("✅ preload 데이터 로딩 성공")
    return data


def get_preload_value(key: str, default: Any = None, path: Optional[str] = None) -> Any:
    try:
        data = load_preload_data(path)
        return data.get(key, default)
    except Exception as e:
        print(f"⚠️ preload 값 가져오기 실패: {e}")
        return default


if __name__ == "__main__":
    print(load_preload_data())
