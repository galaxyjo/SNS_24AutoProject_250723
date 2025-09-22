import pytest
import modules.dm.rules as rules


def test_rule_result_creation():
    result = rules.RuleResult(passed=True, reason="Test passed")
    assert result.passed is True
    assert result.reason == "Test passed"


def test_evaluate_positive_case():
    policy = {"banned": {"scam", "spam"}, "allowed": {"refund", "help"}}
    result = rules.evaluate("I'd like a refund", policy)
    assert isinstance(result, rules.RuleResult)
    assert result.passed is True
    assert "refund" in result.reason


def test_evaluate_negative_case():
    policy = {"banned": {"scam", "spam"}, "allowed": {"refund", "help"}}
    result = rules.evaluate("this is a scam", policy)
    assert isinstance(result, rules.RuleResult)
    assert result.passed is False
    assert "banned word" in result.reason


def test_get_default_policy():
    policy = rules.get_default_policy()
    assert isinstance(policy, dict)
    assert "banned" in policy
    assert "allowed" in policy
    assert "scam" in policy["banned"]
