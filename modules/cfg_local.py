from __future__ import absolute_import
from future.utils import PY2

def load_config():
    if PY2:
        # Python 2 환경일 경우 처리
        print("Running in Python 2 mode")
    else:
        # Python 3 환경일 경우 처리
        print("Running in Python 3 mode")

if __name__ == "__main__":
    load_config()
