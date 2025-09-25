# tests/test_zip_log_exports_6.py
import os
import tempfile
import zipfile
import pytest
from scripts import zip_log_exports_6 as zle


@pytest.fixture
def temp_log_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        # create sample files
        filenames = ["a.db", "b.csv", "c.xlsx", "ignore.txt"]
        for f in filenames:
            with open(os.path.join(tmpdir, f), "w") as fp:
                fp.write("test")
        yield tmpdir


def test_zip_logs_creates_zip(temp_log_dir):
    zip_path = zle.zip_logs(temp_log_dir)
    assert os.path.exists(zip_path)
    with zipfile.ZipFile(zip_path, "r") as zipf:
        namelist = zipf.namelist()
        assert "a.db" in namelist
        assert "b.csv" in namelist
        assert "c.xlsx" in namelist
        assert "ignore.txt" not in namelist


def test_zip_logs_with_custom_path(temp_log_dir):
    custom_zip = os.path.join(temp_log_dir, "custom.zip")
    path = zle.zip_logs(temp_log_dir, export_path=custom_zip)
    assert path == custom_zip
    assert os.path.exists(custom_zip)
