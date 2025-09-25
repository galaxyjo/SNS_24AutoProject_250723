# modules/common/session_core.py
# ============================================================
# 📌 통합 스크립트: session_core.py
# 📂 출처: modules/common/session_1.py
# 📋 역할: 원격 세션 관리 (상태, subscribe/unsubscribe 이벤트)
# ============================================================

from __future__ import annotations
from typing import Any, Dict


def command_builder(method: str, params: Dict) -> Dict:
    """단순한 command dict 생성 (Selenium 의존성 제거 버전)"""
    return {"method": method, "params": params}


class Session:
    def __init__(self, conn: Any):
        self.conn = conn

    def status(self) -> dict:
        cmd = command_builder("session.status", {})
        return self.conn.execute(cmd)

    def subscribe(self, *events: str, browsing_contexts=None) -> dict:
        params = {"events": list(events)}
        if browsing_contexts:
            params["browsingContexts"] = browsing_contexts
        cmd = command_builder("session.subscribe", params)
        return self.conn.execute(cmd)

    def unsubscribe(self, *events: str, browsing_contexts=None) -> dict:
        params = {"events": list(events)}
        if browsing_contexts:
            params["browsingContexts"] = browsing_contexts
        cmd = command_builder("session.unsubscribe", params)
        return self.conn.execute(cmd)


def main():
    print("✅ session_core.py 실행 준비 완료")


if __name__ == "__main__":
    main()
