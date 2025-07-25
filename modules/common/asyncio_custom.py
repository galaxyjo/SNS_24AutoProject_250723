# -*- coding: utf-8 -*-
# modules/common/asyncio_custom.py

from __future__ import annotations
from typing import Coroutine, Any
import asyncio

"""
작업을 하나의 코루틴으로 받아 안전하게 실행해 주는 경량 래퍼.

- run(coro)  : asyncio.run(coro) 래핑
- 최상위 코루틴(예: run_all_accounts(...)) 실행
- RuntimeError("event loop is already running") 예외 대응
- 코루틴의 반환값을 그대로 리턴
"""

def run(coro: Coroutine[Any, Any, Any]) -> Any:
    try:
        return asyncio.run(coro)
    except RuntimeError as exc:
        if "already running" in str(exc):
            loop = asyncio.new_event_loop()
            try:
                asyncio.set_event_loop(loop)
                return loop.run_until_complete(coro)
            finally:
                loop.close()
        raise
