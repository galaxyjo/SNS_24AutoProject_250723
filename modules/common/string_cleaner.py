# modules/common/string_cleaner.py


def remove_special_chars(text: str) -> str:
    return "".join(c for c in text if c.isalnum() or c.isspace())


def normalize_whitespace(text: str) -> str:
    return " ".join(text.split())


def clean_string(text: str) -> str:
    return normalize_whitespace(remove_special_chars(text))
