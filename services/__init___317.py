
---
-----------
--------------------------------------
    ...     ...
    __doc__ += "\n.. autoclass:: numpy.typing.NBitBase\n"
    __doc__ += _docstrings
    >>> array_like: Any = (x**2 for x in range(10))
    >>> def func(a: "np.floating[T]", b: "np.floating[T]") -> "np.floating[T]":
    >>> from typing import Any
    >>> from typing import TypeVar
    >>> import numpy as np
    >>> import numpy.typing as npt
    >>> np.array(array_like)
    >>> np.array(x**2 for x in range(10))
    >>> np.array(x**2 for x in range(10))  # type: ignore
    >>> T = TypeVar("T", bound=npt.NBitBase)
    >>> x = np.array([1, 2])
    >>> x = np.dtype({"field1": (float, 1), "field2": (int, 3)})
    >>> x.dtype = np.bool
    array(<generator object <genexpr> at ...>, dtype=object)
    ArrayLike,
    del _docstrings
    DTypeLike,
    from numpy._typing._add_docstring import _docstrings
    NBitBase,
    NDArray,
  ``formats``, ``names``, ``titles``, ``aligned`` and ``byteorder``.
- `ArrayLike`: objects that can be converted to arrays
- `DTypeLike`: objects that can be converted to dtypes
"""
# further down in this file
# NOTE: The API section will be appended with additional entries
)
* Directly via the ``dtype`` argument.
* With up to five helper arguments that operate via `numpy.rec.format_parser`:
*i.e.* if ``dtype`` is specified than one may not specify ``formats``.
.. _typing-extensions: https://pypi.org/project/typing-extensions/
.. automodule:: numpy.typing.mypy_plugin
.. code-block:: python
.. currentmodule:: numpy.typing
.. versionadded:: 1.20
.. versionadded:: 1.21
__all__ = ["ArrayLike", "DTypeLike", "NBitBase", "NDArray"]
`~numpy.float64` are still sub-types of `~numpy.floating`, but, contrary to
`~numpy.signedinteger`, the former only inheriting from `~numpy.generic`
~~~~~~~
~~~~~~~~~
~~~~~~~~~~~
~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~
============================
0D arrays
0D-array -> scalar cast, then one can consider manually remedying the
addition a number of type aliases are available to users, most prominently
Although this is valid NumPy code, the type checker will complain about it,
API
array. Type checkers will complain about the above example when using
ArrayLike
buggy behavior.
cast are currently annotated as exclusively returning an `~numpy.ndarray`.
combining both dtype specifiers can lead to unexpected or even downright
Consequently, the likes of `~numpy.float16`, `~numpy.float32` and
correct, all operations are that can potentially perform a 0D-array -> scalar
corresponding `~numpy.generic` instance. Until the introduction of shape
del PytestTester
dictionary of fields like below:
Differences from the runtime NumPy API
differences.
DTypeLike
During runtime numpy aggressively casts any passed 0D arrays into their
example,
from numpy._pytesttester import PytestTester
from numpy._typing import (
functions in general, can be specified in one of two ways:
helpful. For that reason, the typed NumPy API is often stricter than
if __doc__ is not None:
If it is known in advance that an operation *will* perform a
involving precision-based casting.
is valid NumPy code which will create a 0-dimensional object
It's possible to mutate the dtype of an array at runtime. For example,
Large parts of the NumPy API have :pep:`484`-style type annotations. In
method to create a view of the array with a different dtype.
Mypy plugin
ndarray
necessary distinction between 0D and >0D arrays. While thus not strictly
Number precision
NumPy is very flexible. Trying to describe the full range of
or explicitly type the array like object as `~typing.Any`:
parameter (see :class:`~NBitBase`), simplifying the annotating of processes
Please see : :ref:`Data type objects <arrays.dtypes>`
possibilities statically would result in types that are not very
Record array dtypes
runtime, they're not necessarily considered as sub-classes.
since its usage is discouraged.
situation with either `typing.cast` or a ``# type: ignore`` comment.
test = PytestTester(__name__)
The `~numpy.timedelta64` class is not considered a subclass of
The `ArrayLike` type tries to avoid creating object arrays. For
The `DTypeLike` type tries to avoid creation of dtype objects using
The dtype of `numpy.recarray`, and the :ref:`routines.array-creation.rec`
the following code is valid:
the NumPy types however. If you really intended to do the above, then
The precision of `numpy.number` subclasses is treated as a invariant generic
the runtime NumPy API. This section describes some notable
the two below:
These two approaches are currently typed as being mutually exclusive,
This sort of mutation is not allowed by the types. Users who want to
Timedelta64
Typing (:mod:`numpy.typing`)
typing (see :pep:`646`) it is unfortunately not possible to make the
while static type checking.
While this mutual exclusivity is not (strictly) enforced during runtime,
write statically typed code should instead use the `numpy.ndarray.view`
you can either use a ``# type: ignore`` comment:
