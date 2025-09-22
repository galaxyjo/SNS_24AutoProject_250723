# -*- coding: utf-8 -*-
def filter_post(content):
    blocked_words = ["scam", "fake", "illegal"]
    return not any(word in content.lower() for word in blocked_words)
