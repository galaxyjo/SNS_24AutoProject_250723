# tests/test_checkpoint.py

import os
import json
import tempfile
import pytest
from modules.core import checkpoint


def test_save_and_load_checkpoint():
    data = {"epoch": 5, "loss": 0.123}
    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = os.path.join(tmpdir, "ckpt.json")
        checkpoint.save_checkpoint(data, filepath)
        loaded = checkpoint.load_checkpoint(filepath)
        assert loaded == data


def test_load_checkpoint_file_not_exists():
    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = os.path.join(tmpdir, "nonexistent.json")
        result = checkpoint.load_checkpoint(filepath)
        assert result is None


def test_load_checkpoint_invalid_json():
    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = os.path.join(tmpdir, "bad.json")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("not valid json")
        result = checkpoint.load_checkpoint(filepath)
        assert result is None
