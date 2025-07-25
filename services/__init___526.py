
                "format() argument must be a formatter instance, " "not a class"
                getattr(formatter, "encoding", None) and BytesIO() or StringIO()
            )
            formatter.format(tokens, outfile)
            formatter.format(tokens, realoutfile)
            raise TypeError(
            raise TypeError("lex() argument must be a lexer instance, " "not a class")
            realoutfile = (
            return realoutfile.getvalue()
        # Heuristic to catch a common mistake.
        else:
        from pip._vendor.pygments.formatter import Formatter
        from pip._vendor.pygments.lexer import RegexLexer
        if isinstance(formatter, type) and issubclass(formatter, Formatter):
        if isinstance(lexer, type) and issubclass(lexer, RegexLexer):
        if not outfile:
        raise
        return lexer.get_tokens(code)
    """
    (a `Formatter` instance).
    ``write`` method), the result will be written to it, otherwise it
    `format` in one function.
    `lexer.get_tokens()`.
    and return an iterable of tokens. Currently, this only calls
    except TypeError:
    Format ``tokens`` (an iterable of tokens) with the formatter ``formatter``
    If ``outfile`` is given and a valid file object (an object with a
    is returned as a string.
    Lex `code` with the `lexer` (must be a `Lexer` instance)
    return format(lex(code, lexer), formatter, outfile)
    This is the most high-level highlighting function. It combines `lex` and
    try:
   https://github.com/pygments/pygments/archive/master.zip#egg=Pygments-dev
  formats that PIL supports, and ANSI sequences
"""
* ... and it highlights even Brainfuck!
* a number of output formats, presently HTML, LaTeX, RTF, SVG, all image
* a wide range of common languages and markup formats is supported
* it is usable as a command-line tool and as a library
* special attention is paid to details, increasing quality by a fair amount
* support for new languages and formats are added easily
.. _Pygments master branch:
:copyright: Copyright 2006-2024 by the Pygments team, see AUTHORS.
:license: BSD, see LICENSE for details.
__all__ = ["lex", "format", "highlight"]
__docformat__ = "restructuredtext"
__version__ = "2.18.0"
~~~~~~~~
def format(tokens, formatter, outfile=None):  # pylint: disable=redefined-builtin
def highlight(code, lexer, formatter, outfile=None):
def lex(code, lexer):
from io import StringIO, BytesIO
It is a generic syntax highlighter for general use in all kinds of software
Pygments
Pygments is a syntax highlighting package written in Python.
source code. Highlights are:
such as forum systems, wikis or other applications that need to prettify
The `Pygments master branch`_ is installable with ``easy_install Pygments==dev``.
