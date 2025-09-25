# modules/common/network_core.py
# 🚀 통합 스크립트
# 출처: network_3.py + emulation_1.py
# 기능: 네트워크 요청/응답 처리 + 환경 에뮬레이션

from typing import Any, Dict, Optional


class NetworkManager:
    """🌐 네트워크 요청/응답 관리"""

    def __init__(self) -> None:
        self.requests: Dict[str, Dict[str, Any]] = {}

    def add_request(self, request_id: str, data: Dict[str, Any]) -> None:
        self.requests[request_id] = data

    def get_request(self, request_id: str) -> Optional[Dict[str, Any]]:
        return self.requests.get(request_id)

    def clear_requests(self) -> None:
        self.requests.clear()
        print("✅ 네트워크 요청 초기화 완료")


class EmulationManager:
    """🖥️ 네트워크/디바이스 에뮬레이션"""

    def __init__(self) -> None:
        self.settings: Dict[str, Any] = {}

    def set_emulation(self, key: str, value: Any) -> None:
        self.settings[key] = value
        print(f"✅ 에뮬레이션 설정 {key} = {value}")

    def get_emulation(self, key: str) -> Optional[Any]:
        return self.settings.get(key)

    def clear_emulation(self) -> None:
        self.settings.clear()
        print("✅ 에뮬레이션 초기화 완료")


if __name__ == "__main__":
    net = NetworkManager()
    emu = EmulationManager()
    net.add_request("1", {"url": "https://example.com", "status": 200})
    print(net.get_request("1"))
    emu.set_emulation("userAgent", "TestBrowser/1.0")
    print(emu.get_emulation("userAgent"))
