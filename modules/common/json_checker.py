import json


def is_valid_json_string(data: str) -> bool:
    try:
        json.loads(data)
        return True
    except (TypeError, ValueError):
        return False


def is_valid_json_file(file_path: str) -> bool:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            json.load(f)
        return True
    except (FileNotFoundError, json.JSONDecodeError, TypeError, ValueError):
        return False
