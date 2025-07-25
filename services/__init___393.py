
    ----------
                blank.join(self._buf + [pre, sep]),
                end=blank,
                file=self._wrapped,
                nolock=nolock,
                np.ndenumerate(iterable), total=total or iterable.size, **tqdm_kwargs
                pass
                tqdm.write(blank.join(self._buf), end=blank, file=self._wrapped)
            )
            blank = type(nl)()
            blank = type(self._buf[0])()
            except (OSError, ValueError):
            return tqdm_class(
            self._buf = [post]
            self._buf.append(x)
            tqdm.write(
            try:
        "This function has no effect, and will be removed in tqdm==5.0.0",
        else:
        if isinstance(iterable, np.ndarray):
        if self._buf:
        if sep:
        import numpy as np
        nl = b"\n" if isinstance(x, bytes) else "\n"
        pass
        pre, sep, post = x.rpartition(nl)
        self._buf = []
        stacklevel=2,
        super().__init__(wrapped)
        TqdmDeprecationWarning,
        yield function(*i)
    """
    """Dummy file-like that will write to tqdm"""
    """Returns `func`"""
    )
    def __del__(self):
    def __init__(self, *args, **kwargs): pass
    def __init__(self, wrapped):
    def write(self, x, nolock=False):
    else:
    Equivalent of `numpy.ndenumerate` or builtin `enumerate`.
    Equivalent of builtin `map`.
    Equivalent of builtin `zip`.
    except ImportError:
    for i in tzip(*sequences, **tqdm_kwargs):
    kwargs = tqdm_kwargs.copy()
    Parameters
    return enumerate(tqdm_class(iterable, total=total, **tqdm_kwargs), start)
    return func
    tqdm_class  : [default: tqdm.auto.tqdm].
    tqdm_class = kwargs.pop("tqdm_class", tqdm_auto)
    try:
    warn(
    yield from zip(tqdm_class(iter1, **kwargs), *iter2plus)
"""
__all__ = ["tenumerate", "tzip", "tmap"]
__author__ = {"github.com/": ["casperdcl"]}
class DummyTqdmFile:
def builtin_iterable(func):
def tenumerate(iterable, start=0, total=None, tqdm_class=tqdm_auto, **tqdm_kwargs):
def tmap(function, *sequences, **tqdm_kwargs):
def tzip(iter1, *iter2plus, **tqdm_kwargs):
from ..auto import tqdm as tqdm_auto
from ..std import TqdmDeprecationWarning, tqdm
from warnings import warn
Subpackages contain potentially unstable extensions.
Thin wrappers around common functions.
