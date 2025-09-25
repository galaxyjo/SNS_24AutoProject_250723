from modules.common.model import DummyModel


def test_dummy_model_init():
    model = DummyModel("User", ["id", "name", "email"])
    assert model.name == "User"
    assert model.fields == ["id", "name", "email"]


def test_dummy_model_to_dict():
    model = DummyModel("User", ["id", "name"])
    result = model.to_dict()
    assert result == {"name": "User", "fields": ["id", "name"]}


def test_dummy_model_repr():
    model = DummyModel("X", ["a"])
    assert "<DummyModel name=X, fields=['a']>" in repr(model)
