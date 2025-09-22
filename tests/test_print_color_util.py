# tests/test_print_color_util.py

from modules.common import print_color_util


def test_color_constants():
    assert print_color_util.Color.RED.startswith("\033")
    assert print_color_util.Color.RESET.endswith("m")


def test_print_color(capsys):
    print_color_util.print_color("Hello", print_color_util.Color.YELLOW)
    captured = capsys.readouterr()
    assert "Hello" in captured.out
    assert "\033" in captured.out
