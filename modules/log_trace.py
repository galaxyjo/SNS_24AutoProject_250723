import time
from datetime import datetime

def get_run_at_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def trace_execution(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            return func(*args, **kwargs)
        finally:
            end = time.time()
            elapsed = end - start
            print(f"⏱ 함수 '{func.__name__}' 실행 시간: {elapsed:.2f}초")
    return wrapper
