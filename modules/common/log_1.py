# modules/common/log_1.py
# ✅ 로그 이벤트 구조 클래스 정의 (삭제하지 말 것)

from dataclasses import dataclass
from typing import List


@dataclass
class ConsoleLogEntry:
    level: str
    method: str
    args: List[dict]
    text: str
    stacktrace: dict
    timestamp: str
    type_: str

    @classmethod
    def from_json(cls, json: dict):
        return cls(
            level=json["level"],
            method=json["method"],
            args=json["args"],
            text=json["text"],
            stacktrace=json["stackTrace"],
            timestamp=json["timestamp"],
            type_=json["type"],
        )


@dataclass
class JavaScriptLogEntry:
    level: str
    method: str
    args: List[dict]
    text: str
    stacktrace: dict
    timestamp: str
    type_: str

    @classmethod
    def from_json(cls, json: dict):
        return cls(
            level=json["level"],
            method=json["method"],
            args=json["args"],
            text=json["text"],
            stacktrace=json["stackTrace"],
            timestamp=json["timestamp"],
            type_=json["type"],
        )


class LogEntryAdded:
    event_class = "log.entryAdded"
