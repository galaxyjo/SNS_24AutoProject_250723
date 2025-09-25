import os
import configparser


def get_config(config_file_path: str = None) -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    if not config_file_path:
        config_file_path = os.path.join(os.path.dirname(__file__), 'config.ini')
    if os.path.exists(config_file_path):
        config.read(config_file_path)
    return config


def get_env_value(section: str, key: str, config_file_path: str = None) -> str:
    config = get_config(config_file_path)
    if config.has_section(section) and config.has_option(section, key):
        return config.get(section, key)
    return None


def set_env_value(section: str, key: str, value: str, config_file_path: str = None) -> None:
    config = get_config(config_file_path)
    if not config.has_section(section):
        config.add_section(section)
    config.set(section, key, value)
    if not config_file_path:
        config_file_path = os.path.join(os.path.dirname(__file__), 'config.ini')
    with open(config_file_path, 'w') as configfile:
        config.write(configfile)
