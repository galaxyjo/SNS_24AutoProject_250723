
"""Sub-package containing the matrix class and related functions."""
__all__ = defmatrix.__all__
del PytestTester
from . import defmatrix
from numpy._pytesttester import PytestTester
test = PytestTester(__name__)
