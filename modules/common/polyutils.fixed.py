
---------
    -----
    ------
    -------
    --------
    ----------
                break
                ret.append(a.copy())
                ret.append(tmp)
                tmp = np.empty(len(a), dtype=np.dtype(object))
                tmp[:] = a[:]
                tmp[0] = mul_f(tmp[0], p[-1])
            6.28318531])
            cc = np.zeros((lmax + 1, c.shape[1]), dtype=c.dtype)
            cc = np.zeros(lmax + 1, dtype=c.dtype)
            dtype = np.common_type(*arrays)
            else:
            exp_format = True
            f"Expected {n_dims} dimensions of sample points, got {len(points)}"
            fractional=True,
            if a.dtype != np.dtype(object):
            if r:
            if seq[i] != 0:
            m, r = divmod(n, 2)
            n = m
            p = mul_f([0] * i + [1], c2)
            p = tmp
            prd = mul_f(prd, c)
            precision=opts["precision"],
            q = rem[-1] / p[-1]
            quo[i] = q
            raise TypeError("expected 1D vector for w")
            raise TypeError("expected x and w to have same length")
            raise ValueError("Coefficient array is empty")
            raise ValueError("Coefficient arrays have no common type") from e
            raise ValueError("ordinates are incompatible")
            raise ValueError("x, y are incompatible")
            raise ValueError("x, y, z are incompatible")
            rem = rem[:-1] - q * p[:-1]
            s = "(" + s + ")"
            sign=opts["sign"] == "+",
            tmp = [mul_f(p[i], p[i + m]) for i in range(m)]
            trim=trim,
            unique=unique,
            x,
        # apply weights. Don't use inplace operations as they
        # can cause problems with NA.
        # in the usual way.
        # This can be made more efficient by using powers of two
        )
        [roots] = as_series([roots], trim=False)
        0 \le j_k &\le \texttt{degrees[k]}
        1-d array containing two values.  If the inputs are complex, then
        1-d array of abscissae whose domain will be determined.
        1-D array of array of series coefficients
        1-d array of coefficients, ordered from lowest order to highest.
        1-d array with trailing zeros removed.  If the resulting series
        1-D arrays.
        a = np.abs(x)
        A 1- or 2-d array_like
        A copy of the input data as a list of 1-d arrays.
        An array of shape ``points[0].shape + tuple(d + 1 for d in degrees)``.
        Array of points of the same shape as `x`, after application of the
        arrays = [trimseq(a) for a in arrays]
        Arrays of point coordinates, all of the same shape. The dtypes
        c = cc
        c = val_f(xi, c)
        c = val_f(xi, c, tensor=False)
        c1[: c2.size] += c2
        c1[: c2.size] -= c2
        c2 = -c2
        c2[: c1.size] += c1
        cc[deg] = c
        containing precisely two values.
        convert to 1-d arrays containing precisely two values.
        deg = np.sort(deg)
        description to include in any error message
        Domains. Each domain must (successfully) convert to a 1-d array
        elif len(args) == 2:
        else:
        except Exception as e:
        for a in arrays:
        for i in range(2, power + 1):
        for i in range(lc1 - lc2, -1, -1):
        for i in range(len(seq) - 1, -1, -1):
        for i in range(n_dims)
        If `tol` < 0
        if a >= 1.0e8 or a < 10 ** min(0, -(opts["precision"] - 1) // 2):
        if a.size == 0:
        if c.ndim == 2:
        if len(args) == 3:
        if len(x) != len(w):
        if parens:
        if w.ndim != 1:
        imin, imax = x.imag.min(), x.imag.max()
        least one of the resulting arrays is empty.
        lhs = lhs * w
        linear map between the two domains.
        lmax = deg
        lmax = deg[-1]
        M &= \texttt{points[k].ndim} \\
        m = \\frac{new[1]-new[0]}{old[1]-old[0]}
        msg = "The fit may be poorly conditioned"
        N &= \texttt{len(points)} = \texttt{len(degrees)} = \texttt{len(vander\_fs)} \\
        n = len(p)
        of the smallest rectangle (aligned with the axes) in the complex
        or may not be a view.
        order = len(deg)
        order = lmax + 1
        p = [line_f(-r, 1) for r in roots]
        plane containing the points `x`. If the inputs are real, then the
        points `x`.
        Points to be mapped. If `x` is a subtype of ndarray the subtype
        prd = c
        quo = np.empty(lc1 - lc2 + 1, dtype=c1.dtype)
        raise TypeError("deg must be an int or non-empty 1-D array of int")
        raise TypeError("expected 1D or 2D array for y")
        raise TypeError("expected 1D vector for x")
        raise TypeError("expected non-empty vector for x")
        raise TypeError("expected x and y to have same length")
        raise TypeError(f"{desc} must be an integer, received {x}") from e
        raise ValueError(
        raise ValueError("Coefficient array is not 1-d")
        raise ValueError("expected deg >= 0")
        raise ValueError("Power is too large")
        raise ValueError("Power must be a non-negative integer.")
        raise ValueError("tol must be non-negative")
        raise ValueError("Unable to guess a dtype or shape when no points are given")
        raise ValueError(f"Expected {n_dims} dimensions of degrees, got {len(degrees)}")
        raise ZeroDivisionError  # FIXME: add message with details to exception
        Raised when `as_series` cannot convert its input to 1-d arrays, or at
        rcond = len(x) * np.finfo(x.dtype).eps
        rem = c1
        ret = []
        ret = [np.array(a, copy=True, dtype=dtype) for a in arrays]
        ret = c1
        ret = c2
        return c
        return c, [resids, rank, s, rcond]
        return c[: ind[-1] + 1].copy()
        return c[:1] * 0
        return c1 / c2[-1], c1[:1] * 0
        return c1[:1] * 0, c1
        return np.array((complex(rmin, imin), complex(rmax, imax)))
        return np.array((x.min(), x.max()))
        return np.array([1], dtype=c.dtype)
        return np.ones(1)
        return operator.index(x)
        return opts["infstr"]
        return opts["nanstr"]
        return p[0]
        return prd
        return quo, trimseq(rem)
        return seq
        return seq[: i + 1]
        return str(x)
        rhs = rhs * w
        rmin, rmax = x.real.min(), x.real.max()
        roots.sort()
        s = dragon4_positional(
        s = dragon4_scientific(
        scl = np.sqrt((np.square(lhs.real) + np.square(lhs.imag)).sum(1))
        scl = np.sqrt(np.square(lhs).sum(1))
        second.
        See the ``<type>div`` functions for more detail
        See the ``<type>fit`` functions for more detail
        See the ``<type>fromroots`` functions for more detail
        See the ``<type>grid<n>d`` functions for more detail
        See the ``<type>pow`` functions for more detail
        See the ``<type>val<n>d`` functions for more detail
        Sequence of Poly series coefficients.
        Subsequence with trailing zeros removed. If the resulting sequence
        than or equal to `tol` (default value is zero) are removed.
        The ``<type>line`` function, such as ``polyline`
        The ``<type>mul`` function, such as ``polymul`
        The ``<type>val`` function, such as ``polyval`
        The 1d vander function to use for each axis, such as ``polyvander`
        The 1d vander function, such as ``polyvander`
        The map ``L(x) = offset + scale*x`` maps the first domain to the
        The maximum degree (inclusive) to use for each axis.
        The two domains that determine the map.  Each must (successfully)
        the two returned points are the lower left and upper right corners
        This must be the same length as `vander_fs`.
        Trailing (i.e., highest order) elements with absolute value less
        trim, unique = "k", False
        try:
        two points are the ends of the smallest interval containing the
        V_k &= \texttt{vander\_fs[k]} \\
        Value to interpret as an integer
        van = vander_f(x, lmax)
        van = vander_f(x, lmax)[:, deg]
        vander_fs[i](points[i], degrees[i])[(...,) + _nth_slice(i, n_dims)]
        w = np.asarray(w) + 0.0
        W[i_0, \ldots, i_M, j_0, \ldots, j_N] = \prod_{k=0}^N{B_{k, j_k}(x_k[i_0, \ldots, i_M])}
        W[i_0, \ldots, i_M, j_0, \ldots, j_N] = \prod_{k=0}^N{V_k(x_k)[i_0, \ldots, i_M, j_k]}
        warnings.warn(msg, RankWarning, stacklevel=2)
        When False, the inputs are passed through intact.
        When True, trailing zeros are removed from the inputs.
        whether any of the elements are complex. Scalars are converted to
        while n > 1:
        will be converted to either float64 or complex128 depending on
        will be preserved.
        would be empty, a series containing a single zero is returned.
        would be empty, return the first element. The returned sequence may
        x = np.asanyarray(x)
        x_k &= \texttt{points[k]} \\
        x\\_out = new[0] + m(x - old[0])
    """
    """Helper function used to implement the ``<type>add`` functions."""
    """Helper function used to implement the ``<type>sub`` functions."""
    """Remove small Poly series coefficients.
    "as_series",
    "format_float",
    "getdomain",
    "mapdomain",
    "mapparms",
    "Small" means "small in absolute value" and is controlled by the
    "trimcoef",
    "trimseq",
    # axis of each in an independent trailing axis of the output
    # c is a trimmed copy
    # c1, c2 are trimmed copies
    # check arguments.
    # convert to the same shape and type
    # Determine the norms of the design matrix columns.
    # Expand c to include non-fitted coefficients which are set to zero
    # produce the vandermonde matrix for each dimension, placing the last
    # set rcond
    # set up the least squares matrices in transposed form
    # Solve the least squares problem.
    # use tensor on only the first
    # warn on rank reduction
    # we checked this wasn't empty already, so no `initial` needed
    ((1+1j), (1-0j))
    (0.0, 1.0)
    (-0.0, -1.0)
    )
    .. math::
    [a1, a2,...] : list of 1-D arrays
    [array([0., 1., 2.]), array([3., 4., 5.])]
    [array([0.]), array([1.]), array([2.]), array([3.])]
    [array([1.]), array([0., 1., 2.]), array([0., 1.])]
    [array([2.]), array([1.1, 0. ])]
    [array([2.]), array([1.1])]
    [c] = as_series([c])
    [c1, c2] = as_series([c1, c2])
    [ind] = np.nonzero(np.abs(c) > tol)
    [x] = as_series([x], trim=False)
    ``[0, 1, 1, 0, 0]`` (which represents ``0 + x + x**2 + 0*x**3 + 0*x**4``)
    `old` to `new` such that ``old[i] -> new[i]``, ``i = 0, 1``.
    >>> a = np.arange(4)
    >>> b = np.arange(6).reshape((2,3))
    >>> c = np.exp(complex(0,1)*np.pi*np.arange(12)/6) # unit circle
    >>> from numpy.polynomial import polyutils as pu
    >>> i = complex(0,1)
    >>> i = complex(0,1) # works for complex
    >>> import numpy as np
    >>> new = (-1 + i, 1 - i)
    >>> new_domain = (0,2*np.pi)
    >>> new_z = pu.mapdomain(z, old, new); new_z
    >>> old = (-1 - i, 1 + i)
    >>> old_domain = (-1,1)
    >>> points = np.arange(4)**2 - 5; points
    >>> pu.as_series((1, np.arange(3), np.arange(2, dtype=np.float16)))
    >>> pu.as_series([2, [1.1, 0.]])
    >>> pu.as_series([2, [1.1, 0.]], trim=False)
    >>> pu.as_series(a)
    >>> pu.as_series(b)
    >>> pu.getdomain(c)
    >>> pu.getdomain(points)
    >>> pu.mapparms((1,-1),(-1,1))
    >>> pu.mapparms((-1,1),(-1,1))
    >>> pu.mapparms((-i,-1),(1,i))
    >>> pu.trimcoef((0,0,1e-3,0,1e-5,0,0),1e-3) # item == tol is trimmed
    >>> pu.trimcoef((0,0,3,0,5,0,0))
    >>> pu.trimcoef((3e-4,1e-3*(1-i),5e-4,2e-5*(1+i)), 1e-3)
    >>> x - pu.mapdomain(x_out, new_domain, old_domain)
    >>> x = np.linspace(-1,1,6); x
    >>> x_out = pu.mapdomain(x, old_domain, new_domain); x_out
    >>> z = np.linspace(old[0], old[1], 6); z
    A generalization of the Vandermonde matrix for N dimensions
    alist : array_like
    Also works for complex numbers (and thus can be used to map any line in
    Also works for complex numbers, and thus can be used to calculate the
    Apply linear map to input points.
    args = [np.asanyarray(a) for a in args]
    array([ 0.        ,  1.25663706,  2.51327412,  3.76991118,  5.02654825, # may vary
    array([0.,  0.,  3.,  0.,  5.])
    array([0., 0., 0., 0., 0., 0.])
    array([0.])
    array([0.0003+0.j   , 0.001 -0.001j])
    array([-1. , -0.6, -0.2,  0.2,  0.6,  1. ])
    array([-1. -1.j , -0.6-0.6j, -0.2-0.2j,  0.2+0.2j,  0.6+0.6j,  1. +1.j ])
    array([-1.0+1.j , -0.6+0.6j, -0.2+0.2j,  0.2-0.2j,  0.6-0.6j,  1.0-1.j ]) # may vary
    array([-1.-1.j,  1.+1.j])
    array([-5, -4, -1,  4])
    array([-5.,  4.])
    array.
    arrays = [np.array(a, ndmin=1, copy=None) for a in alist]
    both the 3-rd and 4-th order coefficients would be "trimmed."
    c : array_like
    c = (c.T / scl).T
    c = val_f(x0, c)
    c, args
    c, resids, rank, s = np.linalg.lstsq(lhs.T / scl, rhs.T, rcond)
    c1, c2
    defined at the values supplied.
    deg = np.asarray(deg)
    degrees : Sequence[int]
    desc : str
    dimension :math:`k`. For a regular polynomial, :math:`B_{k, m}(x) = P_m(x) = x^m`.
    Do not lose the type info if the sequence contains unknown objects.
    domain : ndarray
    Effectively, this implements:
    elif lc2 == 1:
    elif maxpower is not None and power > maxpower:
    elif np.isinf(x):
    elif power == 0:
    elif power == 1:
    else:
    Examples
    except TypeError as e:
    exp_format = False
    Expanding the one-dimensional :math:`V_k` functions gives:
    Find a domain suitable for a polynomial or Chebyshev series
    for a in arrays:
    For some polynomial types, a more efficient approach may be possible.
    for xi in args:
    for xi in it:
    getdomain, mapdomain
    getdomain, mapparms
    Helper function used to implement the ``<type>div`` functions.
    Helper function used to implement the ``<type>fit`` functions.
    Helper function used to implement the ``<type>fromroots`` functions.
    Helper function used to implement the ``<type>grid<n>d`` functions.
    Helper function used to implement the ``<type>pow`` functions.
    Helper function used to implement the ``<type>val<n>d`` functions.
    if any(a.dtype == np.dtype(object) for a in arrays):
    if any(a.ndim != 1 for a in arrays):
    if c2[-1] == 0:
    if deg.min() < 0:
    if deg.ndim == 0:
    if deg.ndim > 0:
    if deg.ndim > 1 or deg.dtype.kind not in "iu" or deg.size == 0:
    if exp_format:
    if full:
    if issubclass(lhs.dtype.type, np.complexfloating):
    if lc1 < lc2:
    if len(c1) > len(c2):
    if len(ind) == 0:
    if len(roots) == 0:
    if len(seq) == 0 or seq[-1] != 0:
    if len(x) != len(y):
    if n_dims != len(degrees):
    if n_dims != len(points):
    if n_dims == 0:
    if not all(a.shape == shape0 for a in args[1:]):
    if not np.issubdtype(type(x), np.floating):
    if np.isnan(x):
    if opts["floatmode"] == "fixed":
    if power != pow or power < 0:
    if rank != order and not full:
    if rcond is None:
    if tol < 0:
    if trim:
    if type(x) not in (int, float, complex) and not isinstance(x, np.generic):
    if w is not None:
    if x != 0:
    if x.dtype.char in np.typecodes["Complex"]:
    if x.ndim != 1:
    if x.size == 0:
    if y.ndim < 1 or y.ndim > 2:
    Implementation uses repeated subtraction of c2 multiplied by the nth basis.
    incorrect type
    it = iter(args)
    lc1 = len(c1)
    lc2 = len(c2)
    lhs = van.T
    Like `_vander_nd`, but flattens the last ``len(degrees)`` axes into a single axis
    Like `operator.index`, but emits a custom exception when passed an
    line therein.
    line_f : function(float, float) -> ndarray
    Linear map parameters between domains.
    mapparms, mapdomain
    mul_f : function(array_like, array_like) -> array_like
    mul_f : function(array_like, array_like) -> ndarray
    n_dims = len(vander_fs)
    newlen = new[1] - new[0]
    Notes
    object.  A 1-d argument of shape ``(N,)`` is parsed into ``N`` arrays of
    of size ``N`` (i.e., is "parsed by row"); and a higher dimensional array
    off = (old[1] * new[0] - old[0] * new[1]) / oldlen
    off, scl = mapparms(old, new)
    offset, scale : scalars
    old, new : array_like
    oldlen = old[1] - old[0]
    opts = np.get_printoptions()
    parameter `tol`; "trailing" means highest order coefficient(s), e.g., in
    Parameters
    parameters required to map any line in the complex plane to any other
    points : Sequence[array_like]
    points = tuple(np.asarray(tuple(points)) + 0.0)
    pow, maxpower
    power = int(pow)
    r"""
    Raises
    raises a Value Error if it is not first reshaped into either a 1-d or 2-d
    Remove "small" "trailing" coefficients from a polynomial.
    Return a domain suitable for given abscissae.
    Return argument as a list of 1-d arrays.
    return c
    return functools.reduce(operator.mul, vander_arrays)
    return off + scl * x
    return off, scl
    return ret
    return s
    Return the parameters of the linear map ``offset + scale*x`` that maps
    return trimseq(ret)
    return tuple(sl)
    return v.reshape(v.shape[: -len(degrees)] + (-1,))
    Returns
    rhs = y.T
    roots
    scl = newlen / oldlen
    scl[scl == 0] = 1
    See Also
    seq : sequence
    series : sequence
    shape0 = args[0].shape
    size one; a 2-d argument of shape ``(M,N)`` is parsed into ``M`` arrays
    sl = [np.newaxis] * ndim
    sl[i] = slice(None)
    the complex plane to any other line therein).
    the domain `new` is applied to the points `x`.
    The linear map ``offset + scale*x`` that maps the domain `old` to
    The result is built by combining the results of 1d Vandermonde matrices,
    The returned list contains array(s) of dtype double, complex double, or
    tol : number, optional
    trim : boolean, optional
    trim, unique = "0", True
    trimmed : ndarray
    try:
    TypeError : if x is a float or non-numeric
    Used to implement the public ``<type>vander<n>d`` functions.
    v = _vander_nd(vander_fs, points, degrees)
    val_f : function(array_like, array_like, tensor: bool) -> array_like
    ValueError
    vander_arrays = (
    vander_f : function(array_like, int) -> ndarray
    vander_fs : Sequence[function(array_like, int) -> ndarray]
    vander_nd : ndarray
    where
    where :math:`B_{k,m}` is the m'th basis of the polynomial construction used along
    x : array_like
    x : int-like
    x = np.asarray(x) + 0.0
    x_out : ndarray
    x0 = next(it)
    y = np.asarray(y) + 0.0
   :toctree: generated/
   as_series    convert list of array_likes into 1-D arrays of common type.
   getdomain    return the domain appropriate for a given set of abscissae.
   mapdomain    maps points between domains.
   mapparms     parameters of the linear map between domains.
   trimcoef     remove small trailing coefficients.
   trimseq      remove trailing zeros.
"""
#
# Helper functions to convert inputs to 1-D arrays
.. autosummary::
]
__all__ = [
and some routines used in both the `polynomial` and `chebyshev` modules.
def _add(c1, c2):
def _as_int(x, desc):
def _div(mul_f, c1, c2):
def _fit(vander_f, x, y, deg, rcond=None, full=False, w=None):
def _fromroots(line_f, mul_f, roots):
def _gridnd(val_f, c, *args):
def _nth_slice(i, ndim):
def _pow(mul_f, c, pow, maxpower):
def _sub(c1, c2):
def _valnd(val_f, c, *args):
def _vander_nd(vander_fs, points, degrees):
def _vander_nd_flat(vander_fs, points, degrees):
def as_series(alist, trim=True):
def format_float(x, parens=False):
def getdomain(x):
def mapdomain(x, old, new):
def mapparms(old, new):
def trimcoef(c, tol=0):
def trimseq(seq):
from numpy._core.multiarray import dragon4_positional, dragon4_scientific
from numpy.exceptions import RankWarning

Functions
import functools
import operator
import warnings

import numpy as np

This module provides: error and warning objects; a polynomial base class;
Utility classes and functions for the polynomial modules.

pass
