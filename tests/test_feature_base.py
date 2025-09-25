# tests/test_feature_base.py
import pytest
from modules.common.feature_base import Feature, Features, features


def test_feature_message_text():
    f = Feature("sample", "pattern", "3.9")
    assert "sample" in f.message_text()
    assert "3.9" in f.message_text()


def test_features_add_and_get():
    f = Feature("alpha", "patternA", "3.6")
    feats = Features()
    feats.add(f)
    assert feats["alpha"] == f
    assert "patternA" in feats.PATTERN


def test_features_global_instance():
    # 기본 제공 features 객체는 최소 1개 이상 Feature 등록됨
    assert isinstance(features.PATTERN, str)
    assert "py3k" in features.PATTERN
