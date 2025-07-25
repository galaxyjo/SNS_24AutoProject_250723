
    ------
    -------
            "A Python re-install with the proper dependencies, "
            "bz2 module not available. "
            "lzma module not available. "
            "might be required to solve this issue."
        "armv"
        )
        If the `bz2` module was not imported correctly, or didn't exist.
        If the `lzma` module was not imported correctly, or didn't exist.
        raise RuntimeError(
        The `BZ2File` class from the `bz2` module.
        The `LZMAFile` class from the `lzma` module.
        True if the running in a continuous integration environment.
        True if the running platform is linux.
        True if the running platform is little endian.
        True if the running platform is mac.
        True if the running platform is windows.
        True if the running platform uses ARM architecture.
    """
    "is_numpy_dev",
    "IS64",
    "ISMUSL",
    "pa_version_under10p1",
    "pa_version_under11p0",
    "pa_version_under13p0",
    "pa_version_under14p0",
    "pa_version_under14p1",
    "pa_version_under16p0",
    "pa_version_under17p0",
    "PY310",
    "PY311",
    "PY312",
    "PYPY",
    )
    Bind the name/qualname attributes of the function.
    bool
    Checking if running in a continuous integration environment by checking
    Checking if the running platform is linux.
    Checking if the running platform is little endian.
    Checking if the running platform is mac.
    Checking if the running platform is windows.
    Checking if the running platform use ARM architecture.
    Checking if the running platform use Power architecture.
    class
    f.__module__ = cls.__module__
    f.__name__ = name
    f.__qualname__ = f"{cls.__name__}.{name}"
    from pandas._typing import F
    if not pandas.compat.compressors.has_bz2:
    if not pandas.compat.compressors.has_lzma:
    Importing the `BZ2File` class from the `bz2` module.
    Importing the `LZMAFile` class from the `lzma` module.
    IS64,
    ISMUSL,
    pa_version_under10p1,
    pa_version_under11p0,
    pa_version_under13p0,
    pa_version_under14p0,
    pa_version_under14p1,
    pa_version_under16p0,
    pa_version_under17p0,
    PY310,
    PY311,
    PY312,
    PYPY,
    Raises
    return f
    return os.environ.get("PANDAS_CI", "0") == "1"
    return pandas.compat.compressors.BZ2File
    return pandas.compat.compressors.LZMAFile
    return platform.machine() in ("arm64", "aarch64") or platform.machine().startswith(
    return platform.machine() in ("ppc64", "ppc64le")
    return sys.byteorder == "little"
    return sys.platform == "darwin"
    return sys.platform == "linux"
    return sys.platform in ["win32", "cygwin"]
    Returns
    RuntimeError
    the PANDAS_CI environment variable.
"""
)
* platform checker
]
__all__ = [
======
compat
Cross-compatible functions for different versions of Python.
def get_bz2_file() -> type[pandas.compat.compressors.BZ2File]:
def get_lzma_file() -> type[pandas.compat.compressors.LZMAFile]:
def is_ci_environment() -> bool:
def is_platform_arm() -> bool:
def is_platform_linux() -> bool:
def is_platform_little_endian() -> bool:
def is_platform_mac() -> bool:
def is_platform_power() -> bool:
def is_platform_windows() -> bool:
def set_function_name(f: F, name: str, cls: type) -> F:
from __future__ import annotations
from pandas.compat._constants import (
from pandas.compat.numpy import is_numpy_dev
from pandas.compat.pyarrow import (
from typing import TYPE_CHECKING
if TYPE_CHECKING:
import os
import pandas.compat.compressors
import platform
import sys
Other items:
