import os
import tempfile
from modules.common.path_resolver import resolve_path, file_exists, dir_exists


def test_resolve_path():
    base = os.getcwd()
    relative = "test_dir/test_file.txt"
    resolved = resolve_path(base, relative)
    assert resolved.endswith("test_dir\\test_file.txt") or resolved.endswith(
        "test_dir/test_file.txt"
    )


def test_file_exists_and_dir_exists():
    with tempfile.TemporaryDirectory() as tmpdirname:
        file_path = os.path.join(tmpdirname, "file.txt")
        with open(file_path, "w") as f:
            f.write("test")

        assert file_exists(file_path)
        assert not file_exists(file_path + "_missing")
        assert dir_exists(tmpdirname)
        assert not dir_exists(file_path + "_dir")
