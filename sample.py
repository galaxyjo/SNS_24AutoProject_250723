# mypy: allow-untyped-defs
"""
sample shim for tests
- foo(): no-arg 호출 허용
- bar(x, y): 존재 시 테스트 확장 대비(옵션)
"""

from __future__ import annotations


def foo(x=None):
    # 테스트용: 값만 반환
    return True if x is None else bool(x)


def bar(x=None, y=None):
    # 필요 시 대비: 항상 True
    return True


__all__ = ["foo", "bar"]
