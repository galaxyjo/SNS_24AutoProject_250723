# modules/common/polyutils.py
import numpy as np
import functools
import operator
import warnings
from numpy.exceptions import RankWarning
from numpy._core.multiarray import dragon4_positional, dragon4_scientific


__all__ = [
    "as_series", "getdomain", "mapdomain", "mapparms", "trimcoef", "trimseq",
    "_add", "_sub", "_div", "_fromroots", "_fit", "_gridnd", "_valnd",
    "_pow", "_vander_nd", "_vander_nd_flat", "_as_int", "format_float",
]


def as_series(alist, trim=True):
    arrays = [np.array(a, ndmin=1, copy=None) for a in alist]
    if not arrays:
        raise ValueError("Coefficient array is empty")
    if any(a.ndim != 1 for a in arrays):
        raise ValueError("Coefficient array is not 1-d")
    try:
        dtype = np.common_type(*arrays)
    except Exception as e:
        raise ValueError("Coefficient arrays have no common type") from e
    arrays = [trimseq(a) for a in arrays]
    if trim:
        arrays = [trimseq(a) for a in arrays]
    return arrays


def getdomain(x):
    x = np.asanyarray(x)
    return np.array((x.min(), x.max()))


def mapparms(old, new):
    old, new = map(np.asanyarray, (old, new))
    off = (old[1]*new[0] - old[0]*new[1]) / (old[1] - old[0])
    scl = (new[1] - new[0]) / (old[1] - old[0])
    return off, scl


def mapdomain(x, old, new):
    off, scl = mapparms(old, new)
    return off + scl * x


def trimcoef(c, tol=0):
    c = np.array(c, ndmin=1)
    if tol < 0:
        raise ValueError("tol must be non-negative")
    if not np.isrealobj(c):
        abs_c = np.absolute(c)
    else:
        abs_c = np.abs(c)
    ind = np.nonzero(abs_c > tol)[0]
    if len(ind) == 0:
        return c[:1]*0
    return c[:ind[-1]+1].copy()


def trimseq(seq):
    seq = np.array(seq, ndmin=1)
    if seq.ndim != 1:
        raise ValueError("expected 1D vector for trimming")
    n = len(seq)
    for i in range(n - 1, -1, -1):
        if seq[i] != 0:
            return seq[:i + 1]
    return seq[:1]*0


def _as_int(x, desc):
    try:
        return operator.index(x)
    except Exception:
        raise TypeError(f"{desc} must be an integer, received {x}")


def format_float(x, parens=False):
    opts = np.get_printoptions()
    s = str(x)
    if parens:
        s = f"({s})"
    return s


def _add(c1, c2):
    c1 = np.atleast_1d(c1)
    c2 = np.atleast_1d(c2)
    if len(c1) < len(c2):
        c1 = np.pad(c1, (0, len(c2) - len(c1)))
    elif len(c2) < len(c1):
        c2 = np.pad(c2, (0, len(c1) - len(c2)))
    return c1 + c2


def _sub(c1, c2):
    c1 = np.atleast_1d(c1)
    c2 = np.atleast_1d(c2)
    if len(c1) < len(c2):
        c1 = np.pad(c1, (0, len(c2) - len(c1)))
    elif len(c2) < len(c1):
        c2 = np.pad(c2, (0, len(c1) - len(c2)))
    return c1 - c2


def _div(mul_f, c1, c2):
    c1 = trimseq(c1)
    c2 = trimseq(c2)
    lc1, lc2 = len(c1), len(c2)
    if lc2 == 0:
        raise ZeroDivisionError
    if lc1 < lc2:
        return c1[:1]*0, c1
    quo = np.empty(lc1 - lc2 + 1, dtype=c1.dtype)
    rem = c1.copy()
    for i in range(lc1 - lc2, -1, -1):
        q = rem[-1] / c2[-1]
        quo[i] = q
        rem[-1] = 0
        rem[lc2 * -1:] -= q * c2
        rem = trimseq(rem)
    return quo, rem


def _pow(mul_f, c, pow, maxpower=None):
    power = _as_int(pow, "power")
    if power < 0:
        raise ValueError("Power must be a non-negative integer.")
    if maxpower is not None and power > maxpower:
        raise ValueError("Power is too large")
    prd = [1]
    for _ in range(power):
        prd = mul_f(prd, c)
    return prd


def _fromroots(line_f, mul_f, roots):
    if len(roots) == 0:
        return np.array([1])
    p = [line_f(-r, 1) for r in roots]
    return functools.reduce(mul_f, p)


def _fit(vander_f, x, y, deg, rcond=None, full=False, w=None):
    x = np.asanyarray(x) + 0.0
    y = np.asanyarray(y) + 0.0
    if x.ndim != 1:
        raise TypeError("expected 1D vector for x")
    if y.ndim < 1 or y.ndim > 2:
        raise TypeError("expected 1D or 2D array for y")
    if x.size == 0:
        raise TypeError("expected non-empty vector for x")
    if x.shape[0] != y.shape[0]:
        raise TypeError("expected x and y to have same length")
    if w is not None:
        w = np.asarray(w) + 0.0
        if w.ndim != 1:
            raise TypeError("expected 1D vector for w")
        if len(x) != len(w):
            raise TypeError("expected x and w to have same length")
    lhs = vander_f(x, deg)
    rhs = y
    if w is not None:
        lhs *= w[:, None]
        rhs *= w[:, None] if rhs.ndim > 1 else w
    scl = np.sqrt(np.square(lhs).sum(1))
    c, resids, rank, s = np.linalg.lstsq(lhs / scl[:, None], rhs, rcond)
    if rank != deg + 1 and not full:
        msg = "The fit may be poorly conditioned"
        warnings.warn(msg, RankWarning)
    return c
# modules/common/polyutils.py

def parse_name(name: str) -> str:
    return name.strip()

def get_domain(email: str) -> str:
    return email.split('@')[-1]

def format_url(url: str) -> str:
    return url.strip().lower()

def generate_uid(name: str, domain: str) -> str:
    return f"{name}_{domain}"
