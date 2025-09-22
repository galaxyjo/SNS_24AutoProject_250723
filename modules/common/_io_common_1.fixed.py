
_core.reschedule(task, outcome.Error(copy.copy(exc)))
                raise_at_end = True
            else:
            if task is current_task:
            setattr(waiters, attr_name, None)
        current_task = _core.current_task()
        current_task = None
        if task is not None:
        raise exc
        task = getattr(waiters, attr_name)
    except RuntimeError:
    for attr_name in ["read_task", "write_task"]:
    from ._io_epoll import EpollWaiters
    from ._io_windows import AFDWaiters
    if raise_at_end:
    raise_at_end = False
    try:
# -*- coding: utf-8 -*-
# Utility function shared between _io_epoll and _io_windows
def wake_all(waiters: EpollWaiters | AFDWaiters, exc: BaseException) -> None:
from __future__ import annotations

from typing import TYPE_CHECKING

from .. import _core

if TYPE_CHECKING:
import copy

import outcome

pass
