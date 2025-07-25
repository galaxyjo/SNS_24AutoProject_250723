
             mask=[False, False, False, True, False, False, False, True],
       invalid operation.
      fill_value=1e+20)
"""
.. [1] Not-a-Number, a floating point value that is the result of an
.. moduleauthor:: Jarrod Millman
.. moduleauthor:: Pierre Gerard-Marchant
__all__ += core.__all__
__all__ += extras.__all__
__all__ = ["core", "extras"]
=============
>>> m
>>> m = np.ma.masked_array(x, np.isnan(x))
>>> np.mean(m)
>>> np.mean(x)
>>> x = np.array([2, 1, 3, np.nan, 5, 2, 3, np.nan])
2.6666666666666665
any number added to ``NaN`` [1]_ produces ``NaN``, this doesn't work.  Enter
arrays fulfill (an example of typical use is given below).
Arrays sometimes contain invalid or missing data.  When doing operations
del PytestTester
For example, examine the following array:
from . import core
from . import extras
from numpy._pytesttester import PytestTester
Here, we construct a masked array that suppress all ``NaN`` values.  We
Masked Arrays
masked arrays:
masked_array(data=[2.0, 1.0, 3.0, --, 5.0, 2.0, 3.0, --],
may now proceed to calculate the mean of the other values:
nan
on such arrays, we wish to suppress invalid values, which is the purpose masked
test = PytestTester(__name__)
The mean is calculated using roughly ``np.sum(x)/len(x)``, but since
When we try to calculate the mean of the data, the result is undetermined:
