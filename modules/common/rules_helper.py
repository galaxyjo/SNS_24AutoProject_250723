# modules/common/rules_helper.py
# ============================================================
# 📌 통합 스크립트: rules_helper.py
# 📂 출처: modules/common/common_rules_2.py, common_rules_3.py
# 📋 역할: 규칙 검증 및 유효성 검사
# ============================================================

import re
from typing import Any


def validate_rule_pattern(text: str, pattern: str) -> bool:
    """주어진 텍스트가 정규식 패턴과 일치하는지 검증"""
    return re.match(pattern, text) is not None


def normalize_rule_key(key: str) -> str:
    """규칙 키 문자열을 소문자+언더스코어 포맷으로 정규화"""
    return key.strip().lower().replace(" ", "_")


def apply_rule(data: dict[str, Any], key: str, pattern: str) -> bool:
    """데이터 dict의 특정 키에 대해 규칙 패턴 검증"""
    if key not in data:
        return False
    return validate_rule_pattern(str(data[key]), pattern)


def merge_rules(base: dict[str, str], overrides: dict[str, str]) -> dict[str, str]:
    """규칙 사전 병합"""
    merged = base.copy()
    merged.update(overrides)
    return merged


def get_default_rules() -> dict[str, str]:
    """기본 규칙 세트"""
    return {
        "email": r"^[\w\.-]+@[\w\.-]+\.\w+$",
        "phone": r"^\+?\d{10,15}$",
        "username": r"^[a-zA-Z0-9_]{3,20}$",
    }


def main() -> None:
    """샘플 실행"""
    rules = get_default_rules()
    sample = {"email": "test@example.com", "phone": "+821012345678"}

    for key, pattern in rules.items():
        result = apply_rule(sample, key, pattern)
        print(f"{key}: {'✅ 통과' if result else '⚠️ 실패'}")


if __name__ == "__main__":
    main()
