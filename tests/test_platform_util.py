import platform
import pytest
from modules.common import platform_util


def test_get_os_name():
    assert platform_util.get_os_name().lower() == platform.system().lower()


def test_is_windows():
    assert platform_util.is_windows() == (platform.system().lower() == "windows")


def test_is_linux():
    assert platform_util.is_linux() == (platform.system().lower() == "linux")


def test_is_mac():
    assert platform_util.is_mac() == (platform.system().lower() == "darwin")
