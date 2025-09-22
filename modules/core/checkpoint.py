# modules/core/checkpoint.py

import os
import json
from typing import Any, Optional


def save_checkpoint(data: Any, path: str) -> None:
    """Save checkpoint data to a JSON file."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_checkpoint(path: str) -> Optional[Any]:
    """Load checkpoint data from a JSON file. Returns None if file doesn't exist."""
    if not os.path.exists(path):
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return None
