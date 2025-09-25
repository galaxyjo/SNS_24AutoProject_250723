import os
import sqlite3
import tempfile
import pytest

from modules.common.storage_1 import insert_storage_data, get_storage_value, ensure_db_initialized


@pytest.fixture
def temp_db_path():
    with tempfile.NamedTemporaryFile(delete=False) as tf:
        yield tf.name
    os.remove(tf.name)


def test_insert_and_retrieve_storage(temp_db_path):
    insert_storage_data("alpha", "123", db_path=temp_db_path)
    value = get_storage_value("alpha", db_path=temp_db_path)
    assert value == "123"


def test_insert_invalid_key(temp_db_path):
    with pytest.raises(ValueError):
        insert_storage_data("", "valid", db_path=temp_db_path)


def test_get_storage_value_not_found(temp_db_path):
    ensure_db_initialized(temp_db_path)
    value = get_storage_value("nonexistent", db_path=temp_db_path)
    assert value is None


def test_ensure_db_initialized_creates_table(temp_db_path):
    ensure_db_initialized(temp_db_path)
    conn = sqlite3.connect(temp_db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='storage_info';")
    result = cursor.fetchone()
    conn.close()
    assert result is not None
