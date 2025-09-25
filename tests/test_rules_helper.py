# tests/test_rules_helper.py
# ============================================================
# 📌 테스트 스크립트: test_rules_helper.py
# 📂 대상: modules/common/rules_helper.py
# ============================================================

import pytest
from modules.common import rules_helper


def test_validate_rule_pattern():
    assert rules_helper.validate_rule_pattern("abc123", r"^[a-z0-9]+$")
    assert not rules_helper.validate_rule_pattern("ABC", r"^[a-z0-9]+$")


def test_normalize_rule_key():
    assert rules_helper.normalize_rule_key(" User Name ") == "user_name"


def test_apply_rule():
    data = {"email": "test@example.com"}
    assert rules_helper.apply_rule(data, "email", r".+@.+")
    assert not rules_helper.apply_rule(data, "missing", r".+")


def test_merge_rules():
    base = {"a": "1"}
    overrides = {"b": "2"}
    merged = rules_helper.merge_rules(base, overrides)
    assert merged["a"] == "1"
    assert merged["b"] == "2"


def test_get_default_rules_and_apply():
    rules = rules_helper.get_default_rules()
    assert "email" in rules
    assert rules_helper.apply_rule({"email": "good@mail.com"}, "email", rules["email"])
