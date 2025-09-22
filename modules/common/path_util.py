# modules/common/path_util.py

import os
from typing import Tuple


def get_filename(path: str) -> str:
    return os.path.basename(path)


def get_directory(path: str) -> str:
    return os.path.dirname(path)


def join_paths(*paths: str) -> str:
    return os.path.join(*paths)


def split_extension(path: str) -> Tuple[str, str]:
    return os.path.splitext(path)


def is_absolute(path: str) -> bool:
    return os.path.isabs(path)
