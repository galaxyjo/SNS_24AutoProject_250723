# C:\SNS_24AutoProject_250723\modules\six_util_custom.py

# modules/six_util_custom.py

from typing import Any, Optional


class SixWrapper:
    """간단한 래퍼/언래퍼 유틸리티."""

    def __init__(self, obj: Optional[Any] = None):
        self.obj = obj

    def wrap(self, content: str) -> str:
        """입력 문자열을 <wrapped> 태그로 감싼다."""
        if not content:
            return "<wrapped></wrapped>"
        return f"<wrapped>{content}</wrapped>"

    def unwrap(self, content: str) -> str:
        """<wrapped>...</wrapped> 형태를 원본 문자열로 복원한다."""
        prefix = "<wrapped>"
        suffix = "</wrapped>"
        if content.startswith(prefix) and content.endswith(suffix):
            return content[len(prefix) : -len(suffix)]
        return content
