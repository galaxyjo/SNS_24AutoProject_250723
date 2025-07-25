
    int(p) for p in re.match(r"(\d+).(\d+).(\d+)", __version__).groups()
)
__all__ = ("__version__", "version_info") + _mock.__all__
__version__ = "5.2.0"
from unittest import mock as _mock
import re
import sys
IS_PYPY = "PyPy" in sys.version
version_info = tuple(
