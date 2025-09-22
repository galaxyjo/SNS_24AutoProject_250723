import traceback


def get_stack_trace_str(exc: Exception) -> str:
    """예외 객체로부터 전체 스택 트레이스를 문자열로 반환"""
    return "".join(traceback.format_exception(type(exc), exc, exc.__traceback__))
