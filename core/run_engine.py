# -*- coding: utf-8 -*-
from __future__ import annotations

from typing import TYPE_CHECKING, overload
from typing_extensions import assert_type
from collections.abc import Sequence  # ✅ 들여쓰기 오류 수정됨

import trio

async def sleep_sort(values: Sequence[float]) -> list[float]:
    return sorted(values)


async def has_optional(arg: int | None = None) -> int:
    return arg if arg is not None else 0


@overload
async def foo_overloaded(arg: int) -> str: ...
@overload
async def foo_overloaded(arg: str) -> int: ...

async def foo_overloaded(arg: int | str) -> int | str:
    if isinstance(arg, str):
        return 5
    return "hello"


if __name__ == "__main__":
    v = trio.run(sleep_sort, (1, 3, 5, 2, 4))
    print("sleep_sort result:", v)

    r1 = trio.run(has_optional)
    print("has_optional() result:", r1)

    r2 = trio.run(has_optional, 5)
    print("has_optional(5) result:", r2)

    r3 = trio.run(foo_overloaded, 5)
    print("foo_overloaded(5) result:", r3)

    r4 = trio.run(foo_overloaded, "")
    print("foo_overloaded(\"\") result:", r4)
