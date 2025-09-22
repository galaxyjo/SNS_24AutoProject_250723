# modules/common/print_color_util.py


class Color:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    RESET = "\033[0m"


def print_color(text: str, color: str = Color.RESET) -> None:
    print(f"{color}{text}{Color.RESET}")
