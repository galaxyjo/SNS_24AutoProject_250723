
return
                    if isinstance(detail, fails):
                # if we are in fails, the ok, otherwise raise it
                getattr(obj, method).__getitem__(axified)
                if fails is not None:
                raise
            # create a tuple accessor
            axified = tuple(new_axes)
            except (IndexError, TypeError, KeyError) as detail:
            new_axes = [slice(None)] * obj.ndim
            new_axes[ax] = key
            try:
        assert axes in [0, 1]
        axes_list = [0, 1]
        axes_list = [axes]
        if ax < obj.ndim:
    Any,
    axes: Literal[0, 1] | None = None,
    else:
    fails=None,
    for ax in axes_list:
    if axes is None:
    key: Any,
    Literal,
    method: Literal["iloc", "loc"],
    obj,
    return [f"{prefix}{i}" for i in range(n)]
"""common utilities"""
)
) -> None:
def _mklbl(prefix: str, n: int):
def check_indexing_smoketest_or_raises(
from __future__ import annotations
from typing import (

pass
