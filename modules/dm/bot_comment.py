from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Dict, Any


@dataclass
class Comment:
    user_id: str
    text: str
    post_id: Optional[str] = None


class BotCommentManager:
    def __init__(self, prefix: str = "[BOT] "):
        self.prefix = prefix

    def send_comment(self, item: Dict[str, Any]) -> bool:
        _ = item.get("id"), item.get("text")
        return True

    def generate_reply(self, comment: Comment) -> str:
        t = (comment.text or "").strip()
        if not t:
            return f"{self.prefix}안녕하세요! 무엇을 도와드릴까요?"
        if "help" in t.lower() or "도움" in t:
            return f"{self.prefix}도움이 필요하시면 키워드 알려주세요."
        return f"{self.prefix}{t} 감사합니다!"


def handle_comment(
    text: str, user_id: str = "unknown", post_id: Optional[str] = None
) -> str:
    mgr = BotCommentManager()
    return mgr.generate_reply(Comment(user_id=user_id, text=text, post_id=post_id))
