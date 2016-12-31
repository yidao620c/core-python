#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Topic: 全局锁/多核
"""

import threading, multiprocessing


def loop():
    x = 0
    while True:
        x = x ^ 1


for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()
