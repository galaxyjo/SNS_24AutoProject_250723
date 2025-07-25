
    """
    """Parse a bytes string into a Message object model.
    """Parse a string into a Message object model.
    """Read a binary file and parse its contents into a Message object model.
    """Read a file and parse its contents into a Message object model.
    "base64mime",
    "charset",
    "encoders",
    "errors",
    "feedparser",
    "generator",
    "header",
    "iterators",
    "message",
    "message_from_binary_file",
    "message_from_bytes",
    "message_from_file",
    "message_from_string",
    "mime",
    "parser",
    "quoprimime",
    "utils",
    from future.backports.email.parser import BytesParser
    from future.backports.email.parser import Parser
    Optional _class and strict are passed to the Parser constructor.
    return BytesParser(*args, **kws).parse(fp)
    return BytesParser(*args, **kws).parsebytes(s)
    return Parser(*args, **kws).parse(fp)
    return Parser(*args, **kws).parsestr(s)
"""
# (Should this be done globally by ``future``?)
# Author: Barry Warsaw
# Contact: email-sig@python.org
# Copyright (C) 2001-2007 Python Software Foundation
# email package.
# Install the surrogate escape handler here because this is used by many
# modules in the email package.
# of importing email since those cascadingly import most of the rest of the
# Some convenience routines.  Don't import Parser and Message as side-effects
]
__all__ = [
__version__ = "5.1.0"
A package for parsing, handling, and generating email messages.
Backport of the Python 3.3 email package for Python-Future.
def message_from_binary_file(fp, *args, **kws):
def message_from_bytes(s, *args, **kws):
def message_from_file(fp, *args, **kws):
def message_from_string(s, *args, **kws):
from future.utils import surrogateescape
surrogateescape.register_surrogateescape()
