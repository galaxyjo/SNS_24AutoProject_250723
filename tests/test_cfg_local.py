import os
import pytest
from modules import cfg_local
from pathlib import Path


def test_get_local_env_existing(monkeypatch):
    monkeypatch.setenv("TEST_KEY", "12345")
    assert cfg_local.get_local_env("TEST_KEY") == "12345"


def test_get_local_env_missing():
    assert cfg_local.get_local_env("NON_EXISTENT_KEY", "fallback") == "fallback"


def test_get_project_root():
    root = cfg_local.get_project_root()
    assert isinstance(root, Path)
    assert root.exists()


def test_get_config_path_default():
    config_path = cfg_local.get_config_path()
    assert isinstance(config_path, Path)
    assert config_path.name == "config.json"


def test_get_config_path_custom():
    custom = cfg_local.get_config_path("custom.yaml")
    assert isinstance(custom, Path)
    assert custom.name == "custom.yaml"
