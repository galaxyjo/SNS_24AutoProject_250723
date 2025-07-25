
"""
"""Common test support for all numpy test scripts.
__all__ = _private.utils.__all__ + ["TestCase", "overrides"]
away.
del PytestTester
from . import _private
from . import overrides
from numpy._pytesttester import PytestTester
from unittest import TestCase
in a single location, so that test scripts can just import it and work right
test = PytestTester(__name__)
This single module should provide all the common functionality for numpy tests
