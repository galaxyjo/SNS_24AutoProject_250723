# tests/test_log_helper.py

from modules.common.log_helper import init_logger, log_info, log_error, log_debug, get_timestamp
import os


def test_logger_creation(tmp_path):
    logger = init_logger("test_logger", log_dir=tmp_path)
    log_info(logger, "Info message")
    log_error(logger, "Error message")
    log_debug(logger, "Debug message")

    log_file = tmp_path / "test_logger.log"
    assert log_file.exists()
    content = log_file.read_text(encoding="utf-8")
    assert "Info message" in content
    assert "Error message" in content
    assert "Debug message" in content


def test_timestamp_format():
    ts = get_timestamp()
    assert len(ts) == 19  # YYYY-MM-DD HH:MM:SS
