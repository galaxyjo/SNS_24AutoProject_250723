# tests/test_shell_util.py

import pytest
from modules.common import shell_util


def test_run_shell_command_success():
    output = shell_util.run_shell_command("echo hello")
    assert output.lower() == "hello"


def test_run_shell_command_failure():
    result = shell_util.run_shell_command("nonexistent_command_xyz")
    assert result is None


def test_run_command_get_code_success():
    code = shell_util.run_command_get_code("exit 0")
    assert code == 0


def test_run_command_get_code_failure():
    code = shell_util.run_command_get_code("exit 123")
    assert code == 123


def test_run_command_get_code_invalid():
    code = shell_util.run_command_get_code("nonexistent_command_xyz")
    assert code != 0  # typically -1
