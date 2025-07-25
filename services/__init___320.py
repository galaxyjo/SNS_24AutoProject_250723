
-------
---------
    $ python3
    ...     pass
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    '\xe5'
    <past.builtins.oldstr>
    >>> # an integer:
    >>> # For example, indexing returns a Python 2-like string object, not
    >>> # List-producing versions of range, reduce, map, filter
    >>> # Other functions removed in Python 3 are resurrected ...
    >>> # This now behaves like a Py2 byte-string on both Py2 and Py3.
    >>> authotranslate('mypy2module')
    >>> execfile('myfile.py')
    >>> for i in xrange(10):
    >>> from past.builtins import execfile
    >>> from past.builtins import range, reduce
    >>> from past.builtins import raw_input
    >>> from past.builtins import reload
    >>> from past.builtins import str as oldstr
    >>> from past.builtins import xrange
    >>> from past.translation import autotranslate
    >>> import mypy2module
    >>> mypy2module.func_taking_py2_string(oldstr(b'abcd'))
    >>> name = raw_input('What is your name? ')
    >>> philosopher = oldstr(u'\u5b54\u5b50'.encode('utf-8'))
    >>> philosopher[0]
    >>> range(10)
    >>> reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
    >>> reload(mymodule)   # equivalent to imp.reload(mymodule) in Python 3
    >>> type(philosopher[0])
    15
    What is your name? [cursor]
  ``past.builtins.str`` type).
  libraries that do not yet wish to upgrade their code properly to Python 3, or
  same APIs as on Python 2 -- particularly with regard to 8-bit strings (the
  wish to upgrade it gradually to Python 3 style.
- as a step in porting a Python 2 codebase to Python 3 (e.g. with the ``futurize`` script)
- to aid in providing minimal-effort Python 3 support for applications using
- to provide Python 3 support for previously Python 2-only libraries with the
"""
:Author:  Ed Schofield, Jordan M. Adler, et al
:Sponsor: Python Charmers: https://pythoncharmers.com
__author__ = "Ed Schofield"
__title__ = "past"
``past`` is a package to aid with Python 2/3 compatibility. Whereas ``future``
===============================================
contains backports of Python 3 constructs to Python 2, ``past`` provides
Copyright 2013-2024 Python Charmers, Australia.
Credits
example::
Here are some code examples that run identically on Python 3 and 2::
implementations of some Python 2 constructs in Python 3 and tools to import and
It also provides import hooks so you can import and use Python 2 modules like
Licensing
past: compatibility with Python 2 from Python 3
Potential uses for libraries:
run Python 2 code in Python 3. It is intended to be used sparingly, as a way of
running old Python 2 code from Python 3 until the code is ported properly.
The software is distributed under an MIT licence. See LICENSE.txt.
this::
until the authors of the Python 2 modules have upgraded their code. Then, for
