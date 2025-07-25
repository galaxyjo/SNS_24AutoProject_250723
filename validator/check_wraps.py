
    assert_type(result, int)
    result = await s.socket.sendto(b"a", "h")
# (except platform independent...)
# -*- coding: utf-8 -*-
# https://github.com/python-trio/trio/issues/2775#issuecomment-1702267589
async def fn(s: trio.SocketStream) -> None:
from typing_extensions import assert_type
import trio
