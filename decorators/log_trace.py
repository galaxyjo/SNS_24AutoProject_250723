import time
from functools import wraps

# 외부 의존성 제거 → 내부에서 직접 run_at 생성
def get_run_at_timestamp():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def log_trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"▶ 실행 시작: {func.__name__}")
        try:
            result = func(*args, **kwargs)
            end = time.time()
            duration = round(end - start, 2)
            print(f"✅ 실행 완료: {func.__name__} (소요시간: {duration}초)")
            return result
        except Exception as e:
            end = time.time()
            duration = round(end - start, 2)
            print(f"❌ 실행 중 오류 발생: {func.__name__} (소요시간: {duration}초)")
            raise e
    return wrapper
