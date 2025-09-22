from modules import cfg_local


def test_set_and_get_config():
    cfg_local.set_config("timeout", 30)
    assert cfg_local.get_config("timeout") == 30


def test_get_config_with_default():
    assert (
        cfg_local.get_config("nonexistent_key", default="default_val") == "default_val"
    )


def test_load_config():
    initial_data = {"host": "localhost", "port": 8080}
    cfg_local.load_config(initial_data)
    assert cfg_local.get_config("host") == "localhost"
    assert cfg_local.get_config("port") == 8080
