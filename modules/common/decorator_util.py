import functools
import time


def timing_decorator(func):
    """함수 실행 시간을 측정하는 데코레이터"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        wrapper.last_runtime = end_time - start_time
        return result

    wrapper.last_runtime = None
    return wrapper


def retry_on_exception(max_retries=3, exceptions=(Exception,), delay=0.1):
    """예외 발생 시 재시도하는 데코레이터"""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_retries:
                        raise
                    time.sleep(delay)

        return wrapper

    return decorator
