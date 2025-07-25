
-----------------
                "",
                f"{'r' if self.releaselevel[0] == 'c' else ''}{self.releaselevel[0]}{self.serial}",
            )[self.releaselevel == "final"]
            + (
            f"{self.major}.{self.minor}.{self.micro}"
        )
        return (
        return f"{__name__} {self.__version__} / {__version_time__}"
        return f"{__name__}.{type(self).__name__}({', '.join('{}={!r}'.format(*nv) for nv in zip(self._fields, self))})"
    "__author__",
    "__compat__",
    "__diag__",
    "__version__",
    "__version_time__",
    "__versionTime__",
    "alphanums",
    "alphas",
    "alphas8bit",
    "And",
    "any_close_tag",
    "any_open_tag",
    "anyCloseTag",
    "anyOpenTag",
    "AtLineStart",
    "AtStringStart",
    "autoname_elements",
    "c_style_comment",
    "CaselessKeyword",
    "CaselessLiteral",
    "Char",
    "CharsNotIn",
    "CloseMatch",
    "col",
    "Combine",
    "common_html_entity",
    "commonHTMLEntity",
    "condition_as_parse_action",
    "conditionAsParseAction",
    "counted_array",
    "countedArray",
    "cpp_style_comment",
    "cppStyleComment",
    "cStyleComment",
    "dbl_quoted_string",
    "dbl_slash_comment",
    "dblQuotedString",
    "dblSlashComment",
    "delimited_list",
    "delimitedList",
    "DelimitedList",
    "Dict",
    "dict_of",
    "dictOf",
    "Each",
    "empty",
    "Empty",
    "FollowedBy",
    "Forward",
    "GoToColumn",
    "Group",
    "Hello,World!", "Hello  ,  World  !", etc.)
    "hexnums",
    "html_comment",
    "htmlComment",
    "identbodychars",
    "identchars",
    "indentedBlock",
    "IndentedBlock",
    "infix_notation",
    "infixNotation",
    "java_style_comment",
    "javaStyleComment",
    "Keyword",
    "line",
    "line_end",
    "line_start",
    "LineEnd",
    "lineEnd",
    "lineno",
    "LineStart",
    "lineStart",
    "Literal",
    "Located",
    "locatedExpr",
    "make_html_tags",
    "make_xml_tags",
    "makeHTMLTags",
    "makeXMLTags",
    "match_only_at_col",
    "match_previous_expr",
    "match_previous_literal",
    "MatchFirst",
    "matchOnlyAtCol",
    "matchPreviousExpr",
    "matchPreviousLiteral",
    "nested_expr",
    "nestedExpr",
    "NoMatch",
    "NotAny",
    "null_debug_action",
    "nullDebugAction",
    "nums",
    "one_of",
    "oneOf",
    "OneOrMore",
    "OnlyOnce",
    "OpAssoc",
    "opAssoc",
    "Opt",
    "Optional",
    "Or",
    "original_text_for",
    "originalTextFor",
    "ParseBaseException",
    "ParseElementEnhance",
    "ParseException",
    "ParseExpression",
    "ParseFatalException",
    "ParserElement",
    "ParseResults",
    "ParseSyntaxException",
    "PositionToken",
    "PrecededBy",
    "printables",
    "punc8bit",
    "pyparsing_common",
    "pyparsing_test",
    "pyparsing_unicode",
    "python_style_comment",
    "pythonStyleComment",
    "quoted_string",
    "QuotedString",
    "quotedString",
    "RecursiveGrammarException",
    "Regex",
    "remove_quotes",
    "removeQuotes",
    "replace_html_entity",
    "replace_with",
    "replaceHTMLEntity",
    "replaceWith",
    "rest_of_line",
    "restOfLine",
    "sgl_quoted_string",
    "sglQuotedString",
    "SkipTo",
    "srange",
    "string_end",
    "string_start",
    "stringEnd",
    "StringEnd",
    "stringStart",
    "StringStart",
    "Suppress",
    "Token",
    "token_map",
    "TokenConverter",
    "tokenMap",
    "trace_parse_action",
    "traceParseAction",
    "ungroup",
    "unicode_set",
    "unicode_string",
    "unicodeString",
    "White",
    "with_attribute",
    "with_class",
    "withAttribute",
    "withClass",
    "Word",
    "WordEnd",
    "WordStart",
    "ZeroOrMore",
    # define grammar of a greeting
    # pre-PEP8 compatibility names
    @property
    _builtin_exprs as common_builtin_exprs,
    def __init__(self, *args, **kwargs): pass
    def __repr__(self):
    def __str__(self):
    def __version__(self):
    from pip._vendor.pyparsing import Word, alphas
    greet = Word(alphas) + "," + Word(alphas) + "!"
    hello = "Hello, World!"
    Hello, World! -> ['Hello', ',', 'World', '!']
    major: int
    micro: int
    minor: int
    print(hello, "->", greet.parse_string(hello))
    pyparsing_common = common  # type: ignore[misc]
    pyparsing_common as common,
    pyparsing_test = testing  # type: ignore[misc]
    pyparsing_unicode = unicode  # type: ignore[misc]
    releaselevel: str
    serial: int
   :class:`CaselessLiteral` classes
   :class:`ParserElement.set_results_name`
   and :class:`'&'<Each>` operators to combine simple expressions into
   and :class:`one_of`
   and :class:`OneOrMore` classes
   class
  - embedded comments
  - extra or missing whitespace (the above program will also handle
   more complex ones
   namespace class
   object
  - quoted strings
 - access the parsed data, which is returned as a :class:`ParseResults`
 - associate names with your parsed results using
 - construct character word-group expressions using the :class:`Word`
 - construct literal match expressions from :class:`Literal` and
 - find more useful common expressions in the :class:`pyparsing_common`
 - find some helpful expression short-cuts like :class:`DelimitedList`
 - see how to create repetitive expressions using :class:`ZeroOrMore`
 - use :class:`'+'<And>`, :class:`'|'<MatchFirst>`, :class:`'^'<Or>`,
"""
#
# "Software"), to deal in the Software without restriction, including
# a copy of this software and associated documentation files (the
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# Copyright (c) 2003-2022  Paul T. McGuire
# define backward compat synonyms
# distribute, sublicense, and/or sell copies of the Software, and to
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# included in all copies or substantial portions of the Software.
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# module pyparsing.py
# Permission is hereby granted, free of charge, to any person obtaining
# permit persons to whom the Software is furnished to do so, subject to
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# The above copyright notice and this permission notice shall be
# the following conditions:
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# without limitation the rights to use, copy, modify, merge, publish,
(the :meth:`'+'<ParserElement.__add__>` operators create :class:`And` expressions,
)
:class:`'|'<MatchFirst>`, :class:`'^'<Or>` and :class:`'&'<Each>` operators.
:class:`Literal`, and :class:`And` elements
:class:`ParserElement.parse_string` can be
]
__all__ = [
__author__ = "Paul McGuire <ptmcg.gm+pyparsing@gmail.com>"
__doc__ = """
__version__ = __version_info__.__version__
__version_info__ = version_info(3, 1, 0, "final", 1)
__version_time__ = "18 Jun 2023 14:05 UTC"
__versionTime__ = __version_time__
``"<salutation>, <addressee>!"``), built up using :class:`Word`,
=============================================================================
a new syntax for defining grammars or matching expressions - the parsing
accessed as a nested list, a dictionary, or an object with named
and the strings are auto-converted to :class:`Literal` expressions)::
attributes.
class version_info:
classes inherit from. Use the docstrings for examples of how to:
core_builtin_exprs += common_builtin_exprs + helper_builtin_exprs
executing simple grammars, vs. the traditional lex/yacc approach, or the
from .actions import *
from .common import (
from .core import *  # type: ignore[misc, assignment]
from .core import __diag__, __compat__
from .core import _builtin_exprs as core_builtin_exprs
from .exceptions import *
from .helpers import *  # type: ignore[misc, assignment]
from .helpers import _builtin_exprs as helper_builtin_exprs
from .results import *
from .testing import pyparsing_test as testing
from .unicode import unicode_set, pyparsing_unicode as unicode
from .util import *
Getting Started -
grammar directly in Python.
Here is a program to parse "Hello, World!" (or any greeting of the form
if "pyparsing_common" not in globals():
if "pyparsing_test" not in globals():
if "pyparsing_unicode" not in globals():
module provides a library of classes that you use to construct the
pyparsing module - Classes and methods to define and execute parsing grammars
see the base classes that most other pyparsing
self-explanatory class names, and the use of :class:`'+'<And>`,
The :class:`ParseResults` object returned from
The program outputs the following::
The pyparsing module handles some of the problems that are typically
The pyparsing module is an alternative approach to creating and
The Python representation of the grammar is quite readable, owing to the
use of regular expressions.  With pyparsing, you don't need to learn
vexing when writing text parsers:
Visit the classes :class:`ParserElement` and :class:`ParseResults` to
