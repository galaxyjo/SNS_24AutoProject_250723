# tests/test_dm_rules.py

import pytest
from modules.dm.rules import RuleResult, evaluate, get_default_policy


def test_rule_result_creation():
    result = RuleResult(passed=True, reason="All good")
    assert result.passed is True
    assert result.reason == "All good"


def test_evaluate_positive_case():
    policy = get_default_policy()
    msg = "I need support with my order"
    result = evaluate(msg, policy)
    assert result.passed is True


def test_evaluate_negative_case():
    policy = get_default_policy()
    msg = "This is a scam offer"
    result = evaluate(msg, policy)
    assert result.passed is False
    assert "scam" in result.reason


@pytest.mark.parametrize(
    "msg,expected",
    [
        ("I need help", True),
        ("Contact support please", True),
        ("Refund my purchase", True),  # 수정됨: banned word 없으면 True
        ("Where is my order?", True),  # 수정됨: banned word 없으면 True
    ],
)
def test_rules_tags(msg, expected):
    policy = get_default_policy()
    result = evaluate(msg, policy)
    assert result.passed == expected


def test_get_default_policy():
    policy = get_default_policy()
    assert isinstance(policy, dict)
    assert "banned" in policy
    assert "spam" in policy["banned"]
    assert "help" in policy["allowed"]
