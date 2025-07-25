
-------
---------
-------------
--------------------
                            print_function, unicode_literals)
             ascii, chr, hex, input, next, oct, open,
             bytes, dict, int, list, object, range, str,
             filter, map, zip)
             pow, round, super,
    >>> # Aliases provided for extensions to existing Py2 module names:
    >>> # etc.
    >>> # Top-level packages with Py3 names provided on Py2:
    >>> from collections import Counter, OrderedDict   # backported to Py2.6
    >>> from collections import UserDict, UserList, UserString
    >>> from future.standard_library import install_aliases
    >>> from itertools import filterfalse, zip_longest
    >>> from subprocess import getoutput, getstatusoutput
    >>> import html.parser
    >>> import queue
    >>> import tkinter.dialog
    >>> import urllib.request
    >>> import xmlrpc.client
    >>> install_aliases()
    from __future__ import (absolute_import, division,
    from builtins import (
"""
:Author:  Ed Schofield, Jordan M. Adler, et al
:Others:  See docs/credits.rst or https://python-future.org/credits.html
:Sponsor: Python Charmers: https://pythoncharmers.com
__author__ = "Ed Schofield"
__copyright__ = "Copyright 2013-2024 Python Charmers (https://pythoncharmers.com)"
__license__ = "MIT"
__title__ = "future"
__ver_major__ = 1
__ver_minor__ = 0
__ver_patch__ = 0
__ver_sub__ = ""
__version__ = "%d.%d.%d%s" % (__ver_major__, __ver_minor__, __ver_patch__, __ver_sub__)
``future`` is the missing compatibility layer between Python 2 and Python
``future`` supports the standard library reorganization (PEP 3108) through the
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<https://python-future.org/automatic_conversion.html>`_ aids in converting
=======================================================
3. It allows you to use a single, clean Python 3.x-compatible codebase to
An included script called `futurize
and builtin functions in ``future``.
Automatic conversion
code (from either Python 2 or Python 3) to code compatible with both
Copyright 2013-2024 Python Charmers, Australia.
corresponding builtins, which normally have different semantics on Python 3
Credits
Documentation
followed by predominantly standard, idiomatic Python 3 code that then runs
following Py3 interfaces:
future: Easy, safe support for Python 2/3 compatibility
It is designed to be used as follows::
Licensing
platforms. It is similar to ``python-modernize`` but goes further in
providing Python 3 compatibility through the use of the backported types
See: https://python-future.org
similarly on Python 2.6/2.7 and Python 3.3+.
Standard library reorganization
support both Python 2 and Python 3 with minimal overhead.
The imports have no effect on Python 3. On Python 2, they shadow the
The software is distributed under an MIT licence. See LICENSE.txt.
versus 2, to provide their Python 3 semantics.
