import os
from typing import Optional

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DEFAULT_CSS_FILENAME = "style.css"


def get_css_path(filename: Optional[str] = None) -> str:
    """
    Return full path to the CSS file, defaulting to DEFAULT_CSS_FILENAME.
    """
    fname = filename or DEFAULT_CSS_FILENAME
    return os.path.join(BASE_DIR, fname)


def load_css(filename: Optional[str] = None) -> str:
    """
    Load CSS content from a file.
    """
    path = get_css_path(filename)
    if not os.path.exists(path):
        raise FileNotFoundError(f"⚠️ CSS file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def save_css(content: str, filename: Optional[str] = None) -> None:
    """
    Save CSS content to a file.
    """
    path = get_css_path(filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ CSS saved to: {path}")


def ensure_default_css() -> None:
    """
    Create a default CSS file if it doesn't exist.
    """
    path = get_css_path()
    if not os.path.exists(path):
        default_css = "body { font-family: sans-serif; background-color: #f9f9f9; }\n"
        save_css(default_css)
        print(f"✅ Default CSS created: {path}")
    else:
        print(f"✅ CSS already exists: {path}")


if __name__ == "__main__":
    ensure_default_css()
