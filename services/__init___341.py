
    "__author__",
    "__email__",
    "__version__",
    "CacheControl",
    "CacheControlAdapter",
    "CacheController",
"""
"""CacheControl import Interface.
#
# SPDX-FileCopyrightText: 2015 Eric Larson
# SPDX-License-Identifier: Apache-2.0
]
__all__ = [
__author__ = "Eric Larson"
__email__ = "eric@ionrock.org"
__version__ = "0.13.1"
from pip._vendor.cachecontrol.adapter import CacheControlAdapter
from pip._vendor.cachecontrol.controller import CacheController
from pip._vendor.cachecontrol.wrapper import CacheControl
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())
Make it easy to import from cachecontrol without long namespaces.
