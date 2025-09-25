# modules/common/log_helper.py
# 출처: log_1.py + script_1.py + check_and_insert_log_2.py 기반 통합

import logging
import os
from datetime import datetime


# ✅ 로그 초기화 함수
def init_logger(name: str = "main", log_dir: str = "logs") -> logging.Logger:
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, f"{name}.log")

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # 콘솔 핸들러
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_fmt = logging.Formatter("📢 [%(levelname)s] %(message)s")
    console_handler.setFormatter(console_fmt)

    # 파일 핸들러
    file_handler = logging.FileHandler(log_path, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    file_handler.setFormatter(file_fmt)

    # 중복 추가 방지
    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger


# ✅ 간단한 로그 유틸 함수
def log_info(logger: logging.Logger, message: str):
    logger.info(message)


def log_error(logger: logging.Logger, message: str):
    logger.error(message)


def log_debug(logger: logging.Logger, message: str):
    logger.debug(message)


# ✅ 타임스탬프만 리턴
def get_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
