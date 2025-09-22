def dedent_block(text: str) -> str:
    """전체 블록의 최소 들여쓰기를 제거한다."""
    lines = text.splitlines()
    stripped_lines = [line for line in lines if line.strip()]
    if not stripped_lines:
        return text
    min_indent = min((len(line) - len(line.lstrip())) for line in stripped_lines)
    return "\n".join(
        line[min_indent:] if len(line) >= min_indent else line for line in lines
    )


def trim_block(text: str) -> str:
    """앞뒤 공백 줄 제거"""
    lines = text.splitlines()
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines)


def remove_duplicate_lines(text: str) -> str:
    """중복 라인을 제거"""
    seen = set()
    result = []
    for line in text.splitlines():
        if line not in seen:
            seen.add(line)
            result.append(line)
    return "\n".join(result)
