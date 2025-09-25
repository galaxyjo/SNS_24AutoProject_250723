import os
import csv
import pytest
from modules.common import _mapping_04f7dcdb

TEST_CSV_PATH = "tests/test_map_temp.csv"

@pytest.fixture(scope="module")
def sample_csv():
    rows = [
        {"old_path": "a.txt", "new_path": "A_final.txt"},
        {"old_path": "b.txt", "new_path": "B_final.txt"},
        {"old_path": "c.txt", "new_path": "C_final.txt"},
    ]
    with open(TEST_CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["old_path", "new_path"])
        writer.writeheader()
        writer.writerows(rows)
    yield TEST_CSV_PATH
    os.remove(TEST_CSV_PATH)

def test_load_mapping_success(sample_csv):
    mapping = _mapping_04f7dcdb.load_mapping_from_csv(sample_csv)
    assert isinstance(mapping, dict)
    assert mapping["a.txt"] == "A_final.txt"
    assert mapping["b.txt"] == "B_final.txt"
    assert mapping["c.txt"] == "C_final.txt"

def test_load_mapping_file_not_exist():
    mapping = _mapping_04f7dcdb.load_mapping_from_csv("nonexistent.csv")
    assert mapping is None

def test_load_mapping_missing_column(tmp_path):
    bad_csv_path = tmp_path / "bad.csv"
    with open(bad_csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["wrong_key", "wrong_value"])
        writer.writerow(["x", "y"])
    mapping = _mapping_04f7dcdb.load_mapping_from_csv(str(bad_csv_path))
    assert mapping is None
