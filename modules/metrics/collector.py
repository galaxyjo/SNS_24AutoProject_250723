"""Metric Collector Module"""

from __future__ import annotations

import random
import time


def collect_metric():
    """Collects a random metric for testing purposes."""
    return {"timestamp": time.time(), "value": random.random()}
