import os
import yaml
import tempfile

from modules.common.yaml_util import load_yaml, dump_yaml


def test_dump_and_load_yaml():
    sample_data = {"name": "SNS", "version": 1.0}
    with tempfile.NamedTemporaryFile(delete=False, suffix=".yaml") as tmp_file:
        tmp_path = tmp_file.name

    try:
        dump_yaml(sample_data, tmp_path)
        loaded_data = load_yaml(tmp_path)
        assert loaded_data == sample_data
    finally:
        os.remove(tmp_path)
