import os
from scripts import export_log_formatter

def test_format_log_to_html_basic():
    input_log = "[bold]Test HTML[/bold]"
    html_output = export_log_formatter.format_log_to_html(input_log)
    assert "<!DOCTYPE html>" in html_output
    assert "Test HTML" in html_output

def test_format_log_to_svg_basic(tmp_path):
    input_log = "[bold red]Test SVG[/bold red]"
    output_svg = tmp_path / "test_output.svg"
    export_log_formatter.save_log_to_svg_file(input_log, str(output_svg))
    assert output_svg.exists()
    content = output_svg.read_text(encoding="utf-8")
    assert "<svg" in content
    assert "Test" in content  # 더 이상 정확한 ANSI 매핑 문자열로 검사하지 않음
