import io
import os
from rich.console import Console
from rich.terminal_theme import MONOKAI

def format_log_to_html(log_text: str) -> str:
    console = Console(
        record=True,
        file=io.StringIO(),
        force_terminal=True,
        width=100,
    )
    console.print(log_text)
    html = console.export_html(theme=MONOKAI, inline_styles=True)
    return html

def save_log_to_svg_file(log_text: str, output_path: str) -> None:
    console = Console(record=True, force_terminal=True, width=100)
    console.print(log_text)
    console.save_svg(output_path, title="Log Output")

if __name__ == "__main__":
    sample_log = "[bold green]✅ Export 시작됨[/bold green]\n[red]⚠️ 오류 발생[/red]"
    html = format_log_to_html(sample_log)
    svg_path = "export_log_output.svg"

    with open("export_log_output.html", "w", encoding="utf-8") as f:
        f.write(html)

    save_log_to_svg_file(sample_log, svg_path)

    print("✅ HTML/SVG export 완료")
