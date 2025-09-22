# 📄 modules/cfg_local.py (리팩토링 후 전체 복붙용)
"""Configuration management module for local settings."""

import os
from pathlib import Path
from typing import Any


class LocalConfig:
    """Encapsulated configuration manager to avoid global state."""

    def __init__(self):
        self._config = {}

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value by key, with optional default."""
        return self._config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set a configuration value by key."""
        self._config[key] = value

    def load(self, initial_data: dict = None) -> None:
        """Load initial configuration from a dictionary."""
        if initial_data:
            self._config.update(initial_data)


def get_local_env(key: str, default: Any = None) -> Any:
    """Fetch value from environment or fallback to default."""
    return os.getenv(key, default)


def get_project_root() -> Path:
    """Return the project root path."""
    return Path(__file__).resolve().parent.parent


def get_config_path(filename: str = "config.json") -> Path:
    """Return full config path."""
    return get_project_root() / filename


# Optional shared instance (not mandatory)
CONFIG = LocalConfig()
# 📄 modules/cfg_local.py (파일 마지막에 추가)
CONFIG = LocalConfig()

# 호환성 유지용 shim 함수
get_config = CONFIG.get
set_config = CONFIG.set
load_config = CONFIG.load
