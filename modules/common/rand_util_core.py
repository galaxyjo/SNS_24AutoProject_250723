# -*- coding: utf-8 -*-
import random
import string
import uuid
import time

def random_string(length=12):
    """랜덤 문자열 생성 (영문+숫자)"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def random_delay(min_sec=1.0, max_sec=3.0):
    """무작위 딜레이 (초)"""
    delay = random.uniform(min_sec, max_sec)
    time.sleep(delay)

def generate_uuid():
    """UUID 문자열 생성"""
    return str(uuid.uuid4())

def random_int(min_val=0, max_val=100):
    """정수 범위 내 랜덤 값"""
    return random.randint(min_val, max_val)

def random_float(min_val=0.0, max_val=1.0):
    """부동소수점 랜덤 값"""
    return random.uniform(min_val, max_val)
