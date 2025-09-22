# path: modules/dm/mention_handler.py
from __future__ import annotations

from typing import Dict

from .logger import get_logger
from .rules import evaluate
from .types import ActionResult, InboundEvent

logger = get_logger(__name__)


async def handle_mention(event: InboundEvent) -> ActionResult:
    rr = evaluate(event.text)
    if not rr.allowed:
        logger.info("mention blocked id=%s reason=%s", event.id, rr.matched)
        return ActionResult(
            ok=False, action="blocked", reason="banned", data={"matched": rr.matched}
        )
    reply = _basic_reply(event.text, rr.tags)
    logger.info("mention reply id=%s tags=%s", event.id, rr.tags)
    return ActionResult(ok=True, action="reply", data={"text": reply, "tags": rr.tags})


def _basic_reply(text: str, tags: Dict | list) -> str:
    if "help" in tags or "support" in tags:
        return " 감사합니다. 곧 지원팀이  도와드리겠습니다."
    if "order" in tags:
        return "주문 관련 문의로 확인했습니다. 상세 정보를 알려주세요."
    if "refund" in tags:
        return "환불 절차를 안내드리겠습니다. 주문번호를 알려주세요."
    return "멘션 감사드립니다. 무엇을 도와드릴까요?"
