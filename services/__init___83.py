
        "ascii",
        "bytes",
        "chr",
        "dict",
        "filter",
        "hex",
        "input",
        "int",
        "list",
        "map",
        "max",
        "min",
        "next",
        "object",
        "oct",
        "open",
        "pow",
        "range",
        "round",
        "str",
        "super",
        "zip",
    # No namespace pollution on Py3
    # Only shadow builtins on Py2; no new names
    # pollution on Py2.
    # We only import names that shadow the builtins on Py2. No other namespace
    ]
    __all__ = [
    __all__ = []
    bytes = builtins.bytes
    dict = builtins.dict
    import builtins
    int = builtins.int
    list = builtins.list
    object = builtins.object
    pass
    range = builtins.range
    str = builtins.str
"""
# backward-compatibility with future v0.8.2. It will be removed in future v1.0.
# The isinstance import is no longer needed. We provide it only for
(``docs/what-else.rst``) for more information.
A module that brings in equivalents of the new and modified Python 3
builtins into Py2. Has no effect on Py3.
else:
from future import utils
from future.utils import PY3
if not utils.PY3:
if PY3:
See the docs `here <https://python-future.org/what-else.html>`_
