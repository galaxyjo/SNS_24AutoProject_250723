
        "apply",
        "basestring",
        "chr",
        "cmp",
        "dict",
        "execfile",
        "filter",
        "intern",
        "long",
        "map",
        "range",
        "raw_input",
        "reduce",
        "reload",
        "str",
        "unichr",
        "unicode",
        "xrange",
        "zip",
    # No namespace pollution on Py2
    # Only shadow builtins on Py3; no new names
    # pollution on Py3.
    # We only import names that shadow the builtins on Py3. No other namespace
    ]
    __all__ = [
    __all__ = []
    pass
- apply
- basestring
- chr
- cmp
- dict
- execfile
- filter
- intern <- sys.intern
- long
- map
- range
- raw_input <- input
- reduce <- functools.reduce
- reload <- imp.reload
- str
- unichr <- chr
- unicode
- unicode <- str
- xrange <- range
- zip
"""
# from past.builtins.misc import (ascii, hex, input, oct, open)
1. Implementations of these builtin functions which have no equivalent on Py3:
2. Aliases:
3. List-producing versions of the corresponding Python 3 iterator-producing functions:
4. Forward-ported Py2 types:
A resurrection of some old functions from Python 2 for use in Python 3. These
else:
from future.utils import PY3
from past import utils
if PY3:
if utils.PY3:
is no longer standard Python 3 code.
should be used sparingly, to help with porting efforts, since code using them
This module provides the following:
