# path: modules/dm/logger.py
from __future__ import annotations

import logging
import os
from typing import Optional

_LOGGER_NAME = "sns24.dm"


def get_logger(name: Optional[str] = None) -> logging.Logger:
    logger = logging.getLogger(name or _LOGGER_NAME)
    if not logger.handlers:
        level = os.getenv("SNS24_LOG_LEVEL", "INFO").upper()
        logger.setLevel(getattr(logging, level, logging.INFO))
        handler = logging.StreamHandler()
        fmt = "[%(asctime)s] %(levelname)s %(name)s - %(message)s"
        handler.setFormatter(logging.Formatter(fmt))
        logger.addHandler(handler)
        logger.propagate = False
    return logger
