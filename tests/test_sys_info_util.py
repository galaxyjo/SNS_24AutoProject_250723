# tests/test_sys_info_util.py

from modules.common.sys_info_util import (
    get_platform_info,
    get_python_version,
    get_cpu_count,
    is_windows,
    is_linux,
)


def test_get_platform_info():
    info = get_platform_info()
    assert isinstance(info, str)
    assert len(info) > 0


def test_get_python_version():
    version = get_python_version()
    assert "Python" not in version  # raw version string
    assert isinstance(version, str)


def test_get_cpu_count():
    count = get_cpu_count()
    assert isinstance(count, int)
    assert count >= 1


def test_os_flags():
    win = is_windows()
    linux = is_linux()
    assert win or linux  # at least one must be true
