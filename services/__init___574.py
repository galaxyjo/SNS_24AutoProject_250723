
    "SortedDict",
    "SortedItemsView",
    "SortedKeyList",
    "SortedKeysView",
    "SortedList",
    "SortedListWithKey",
    "SortedSet",
    "SortedValuesView",
    ('c', 3)
    ['e', 'e', 'e']
    >>> from sortedcontainers import SortedDict
    >>> from sortedcontainers import SortedList
    >>> from sortedcontainers import SortedSet
    >>> sd
    >>> sd = SortedDict({'c': 3, 'a': 1, 'b': 2})
    >>> sd.popitem(index=-1)
    >>> sl
    >>> sl *= 1000000
    >>> sl = SortedList(['e', 'a', 'c', 'd', 'b'])
    >>> sl.count('c')
    >>> sl[-3:]
    >>> ss
    >>> ss = SortedSet('abracadabra')
    >>> ss.bisect_left('c')
    1000000
    2
    SortedDict({'a': 1, 'b': 2, 'c': 3})
    SortedDict,
    SortedItemsView,
    SortedKeysView,
    SortedList(['a', 'b', 'c', 'd', 'e'])
    SortedSet(['a', 'b', 'c', 'd', 'r'])
    SortedValuesView,
"""
"""Sorted Containers -- Sorted List, Sorted Dict, Sorted Set
)
::
:copyright: (c) 2014-2019 by Grant Jenks.
:license: Apache 2.0, see LICENSE for more details.
]
__all__ = [
__author__ = "Grant Jenks"
__build__ = 0x020400
__copyright__ = "2014-2019, Grant Jenks"
__license__ = "Apache 2.0"
__title__ = "sortedcontainers"
__version__ = "2.4.0"
and benchmarking.
different implementations, most using C-extensions without great documentation
from .sorteddict import (
from .sortedlist import SortedList, SortedKeyList, SortedListWithKey
from .sortedset import SortedSet
In Python, we can do better. And we can do it in pure-Python!
or pre-build and distribute custom extensions. Performance is a feature and
pure-Python, and fast as C-extensions.
Python's standard library is great until you need a sorted collections
Sorted Containers is an Apache2 licensed containers library, written in
Sorted Containers takes all of the work out of Python sorted types - making
testing has 100% coverage with unit tests and hours of stress.
type. Many will attest that you can get really far without one, but the moment
you **really need** a sorted list, dict, or set, you're faced with a dozen
your deployment and use of Python easy. There's no need to install a C compiler
