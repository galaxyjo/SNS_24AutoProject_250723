import os
import datetime
from dotenv import load_dotenv

# 환경변수 로드
load_dotenv()

# BASE_DIR 설정 (env → fallback)
BASE_DIR = os.getenv("BASE_PATH", os.path.dirname(os.path.abspath(__file__)))


def get_local_datetime_now(fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
    현재 로컬 시간을 지정된 형식으로 반환합니다.

    Args:
        fmt (str): 시간 포맷 문자열 (기본값: "%Y-%m-%d %H:%M:%S")

    Returns:
        str: 포맷된 현재 시간 문자열
    """
    try:
        now = datetime.datetime.now()
        return now.strftime(fmt)
    except Exception as e:
        print("⚠️ get_local_datetime_now() 실패:", e)
        raise


def get_local_datetime_compact(fmt: str = "%Y%m%d_%H%M%S") -> str:
    """
    파일명 등에 사용하기 적합한 Compact한 현재 시간을 반환합니다.

    Args:
        fmt (str): 시간 포맷 문자열 (기본값: "%Y%m%d_%H%M%S")

    Returns:
        str: 포맷된 현재 시간 문자열
    """
    try:
        now = datetime.datetime.now()
        return now.strftime(fmt)
    except Exception as e:
        print("⚠️ get_local_datetime_compact() 실패:", e)
        raise


# 단독 실행 디버깅용
if __name__ == "__main__":
    print("✅ get_local_datetime_now:", get_local_datetime_now())
    print("✅ get_local_datetime_compact:", get_local_datetime_compact())
