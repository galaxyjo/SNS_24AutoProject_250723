import os
import json


def load_config(path: str = "config.json", default: dict = None) -> dict:
    """
    지정된 경로에서 JSON 설정 파일을 불러오고 파싱하여 반환.
    오류 발생 시 기본값 반환.
    """
    if default is None:
        default = {}

    if not os.path.exists(path):
        return default

    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return default
