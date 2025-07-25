
----
--------
---------
----------
    -----
    --------
    ----------
            f"and 'unicode'"
            f"Unsupported format string '{style}'. Valid options are 'ascii' "
        )
        _use_unicode = False
        Format string for default printing style. Must be either 'ascii' or
        raise ValueError(
        'unicode'.
    """
    "chebyshev",
    "Chebyshev",
    "hermite",
    "Hermite",
    "hermite_e",
    "HermiteE",
    "Laguerre",
    "laguerre",
    "legendre",
    "Legendre",
    "Polynomial",
    "polynomial",
    "set_default_printstyle",
    _use_unicode = True
    >>> # Formatting supersedes all class/package-level defaults
    >>> c = chebfit(xdata, ydata, deg=1)
    >>> c = Chebyshev.fit(xdata, ydata, deg=1)
    >>> c = np.polynomial.Chebyshev([1, 2, 3])
    >>> from numpy.polynomial import Chebyshev
    >>> from numpy.polynomial.chebyshev import chebfit
    >>> np.polynomial.set_default_printstyle('ascii')
    >>> np.polynomial.set_default_printstyle('unicode')
    >>> p = np.polynomial.Polynomial([1, 2, 3])
    >>> print(c)
    >>> print(f"{p:unicode}")
    >>> print(p)
    >>> xdata = [1, 2, 3, 4]
    >>> ydata = [1, 4, 9, 16]
    1.0 + 2.0 T_1(x) + 3.0 T_2(x)
    1.0 + 2.0 x + 3.0 x**2
    1.0 + 2.0·T₁(x) + 3.0·T₂(x)
    1.0 + 2.0·x + 3.0·x²
    ABCPolyBase._use_unicode = _use_unicode
    default font support for the unicode superscript and subscript ranges.
    Examples
    from ._polybase import ABCPolyBase
    if style == "ascii":
    if style not in ("unicode", "ascii"):
    Notes
    or 'unicode'.
    Parameters
    Set the default format for the string representation of polynomials.
    style : str
    The default format depends on the platform: 'unicode' is used on
    Unix-based systems and 'ascii' on Windows. This determination is based on
    Values for ``style`` must be valid inputs to ``__format__``, i.e. 'ascii'
  ``domain`` and ``window``.
  between ``domain`` and ``window``
  determined by the least-squares fit to the data ``x``, ``y``
- ``p.cast(Poly)``    -- Convert ``p`` to instance of kind ``Poly``
- ``p.convert(Poly)`` -- Convert ``p`` to instance of kind ``Poly`` or map
- ``p.copy()``              -- Create a copy of ``p``
- ``p.cutdeg(degree)`` -- Truncate ``p`` to given degree
- ``p.deriv()`` -- Take the derivative of ``p``
- ``p.integ()`` -- Integrate ``p``
- ``p.linspace()`` -- Return ``x, p(x)`` at equally-spaced points in ``domain``
- ``p.mapparms()`` -- Return the parameters for the linear mapping between
- ``p.roots()``    -- Return the roots of ``p``.
- ``p.trim()``     -- Remove trailing coefficients.
- ``p.truncate(size)`` -- Truncate ``p`` to given size
- ``Poly.basis(degree)``    -- Basis polynomial of given degree
- ``Poly.basis_name`` -- String used to represent the basis
- ``Poly.domain``     -- Default domain
- ``Poly.fit(x, y, deg)``   -- ``p`` of degree ``deg`` with coefficients
- ``Poly.fromroots(roots)`` -- ``p`` with specified roots
- ``Poly.has_samecoef(p1, p2)``   -- Check if coefficients match
- ``Poly.has_samedomain(p1, p2)`` -- Check if domains match
- ``Poly.has_sametype(p1, p2)``   -- Check if types match
- ``Poly.has_samewindow(p1, p2)`` -- Check if windows match
- ``Poly.identity()``       -- ``p`` where ``p(x) = x`` for all ``x``
- ``Poly.maxpower``   -- Maximum value ``n`` such that ``p**n`` is allowed
- ``Poly.nickname``   -- String used in printing
- ``Poly.window``     -- Default window
"""
"wraps" the "standard" basis) or `chebyshev`.  For optimal performance,
**Name**                    **Provides**
]
__all__ = [
``np.polynomial.chebyshev.Chebyshev``, respectively.
``np.polynomial.chebyshev`` module::
``np.polynomial.polynomial.Polynomial`` or
``np.polynomial.Polynomial`` or ``np.polynomial.Chebyshev`` instead of
``P_0 + 2*P_1 + 3*P_2``, where P_n is the n-th order basis polynomial
`~chebyshev.Chebyshev.fit` class method::
`~chebyshev.Chebyshev`      Chebyshev series
`~hermite.Hermite`          Hermite series
`~hermite_e.HermiteE`       HermiteE series
`~laguerre.Laguerre`        Laguerre series
`~legendre.Legendre`        Legendre series
`~polynomial.Polynomial`    Power series
`~polynomial.Polynomial`, `~chebyshev.Chebyshev`, `~hermite.Hermite`, etc.)
===================
========================    ================
A sub-package for efficiently dealing with polynomials.
all operations on polynomials, including evaluation at an argument, are
applicable to the specific module in question, e.g., `polynomial` (which
by a 1-D numpy array of the polynomial's coefficients, ordered from lowest
by arrays ``xdata`` and ``ydata``, the
Calculus
Constants
Convenience Classes
Conversion
Creation
def set_default_printstyle(style):
del PytestTester
For example, to fit a Chebyshev polynomial with degree ``1`` to data given
from .chebyshev import Chebyshev
from .hermite import Hermite
from .hermite_e import HermiteE
from .laguerre import Laguerre
from .legendre import Legendre
from .polynomial import Polynomial
from numpy._pytesttester import PytestTester
i.e., a polynomial (also referred to simply as a "series") is represented
implemented as operations on the coefficients.  Additional (module-specific)
information can be found in the docstring for the module of interest.
is preferred over the `chebyshev.chebfit` function from the
manipulating, and fitting data with polynomials of different bases.
Methods for converting a polynomial instance of one kind to another.
Methods for creating polynomial instances.
Misc
of polynomials:
order term to highest.  For example, array([1,2,3]) represents
package, and are available from the ``numpy.polynomial`` namespace.
See :doc:`routines.polynomials.classes` for more details.
test = PytestTester(__name__)
The classes provide a more consistent and concise interface than the
the classes representing the various kinds of polynomials. In the following,
The convenience classes are the preferred interface for the `~numpy.polynomial`
The following lists the various constants and methods common to all of
the term ``Poly`` represents any one of the convenience classes (e.g.
These *convenience classes* provide a consistent interface for creating,
This eliminates the need to navigate to the corresponding submodules, e.g.
This package provides *convenience classes* for each of six different kinds
type-specific functions defined in the submodules for each type of polynomial.
Validation
while the lowercase ``p`` represents an **instance** of a polynomial class.
Within the documentation for this sub-package, a "finite power series,"
