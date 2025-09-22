# modules/dm/echo.py


def handle_dm(text):
    if not text:
        return "No input"
    if "refund" in text.lower():
        return "We will process your refund."
    return "Thank you for your message."
