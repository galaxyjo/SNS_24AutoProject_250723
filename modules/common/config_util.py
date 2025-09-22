import json
import os
from typing import Any


def load_config(file_path: str) -> dict[str, Any]:
    if not os.path.exists(file_path):
        return {}
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_config_value(config: dict[str, Any], key: str, default: Any = None) -> Any:
    return config.get(key, default)
