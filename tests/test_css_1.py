import os
import tempfile
import shutil

from modules.common import css_1


def test_get_css_path():
    path = css_1.get_css_path("test.css")
    assert path.endswith("test.css")


def test_save_and_load_css():
    temp_dir = tempfile.mkdtemp()
    original_dir = css_1.BASE_DIR
    try:
        css_1.BASE_DIR = temp_dir
        content = "body { color: red; }"
        css_1.save_css(content, "temp.css")
        loaded = css_1.load_css("temp.css")
        assert loaded.strip() == content
    finally:
        css_1.BASE_DIR = original_dir
        shutil.rmtree(temp_dir)


def test_ensure_default_css():
    temp_dir = tempfile.mkdtemp()
    original_dir = css_1.BASE_DIR
    try:
        css_1.BASE_DIR = temp_dir
        css_path = css_1.get_css_path()
        assert not os.path.exists(css_path)
        css_1.ensure_default_css()
        assert os.path.exists(css_path)
    finally:
        css_1.BASE_DIR = original_dir
        shutil.rmtree(temp_dir)
