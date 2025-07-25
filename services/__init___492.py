
    "__version__",
    "CharsetMatch",
    "CharsetMatches",
    "detect",
    "from_bytes",
    "from_fp",
    "from_path",
    "is_binary",
    "set_logging_handler",
    "VERSION",
   >>> best_guess = results.best()
   >>> from charset_normalizer import from_bytes
   >>> results = from_bytes('Bсеки човек има право на образование. Oбразованието!'.encode('utf_8'))
   >>> str(best_guess)
   'Bсеки човек има право на образование. Oбразованието!'
"""
# Attach a NullHandler to the top level logger by default
# https://docs.python.org/3.3/howto/logging.html#configuring-logging-for-a-library
)
:copyright: (c) 2021 by Ahmed TAHRI
:license: MIT, see LICENSE for more details.
__all__ = (
~~~~~~~~~~~~~~
A library that helps you read text from an unknown charset encoding.
All IANA character set names for which the Python core library provides codecs are supported.
at <https://github.com/Ousret/charset_normalizer>.
Basic usage:
Charset-Normalizer
from .api import from_bytes, from_fp, from_path, is_binary
from .legacy import detect
from .models import CharsetMatch, CharsetMatches
from .utils import set_logging_handler
from .version import VERSION, __version__
from __future__ import annotations
import logging
logging.getLogger("charset_normalizer").addHandler(logging.NullHandler())
Motivated by chardet, This package is trying to resolve the issue by taking a new approach.
Others methods and usages are available - see the full documentation
The Real First Universal Charset Detector.
