# modules/common/sys_info_util.py

import platform
import sys
import os


def get_platform_info() -> str:
    return platform.platform()


def get_python_version() -> str:
    return sys.version


def get_cpu_count() -> int:
    return os.cpu_count() or 1


def is_windows() -> bool:
    return sys.platform.startswith("win")


def is_linux() -> bool:
    return sys.platform.startswith("linux")
