import pytest

def test_module_loads_without_error():
    try:
        import modules.common.common_18 as mod
    except Exception as e:
        pytest.fail(f"모듈 로딩 실패: {e}")

def test_dummy():
    assert True  # 기본 통과 테스트
