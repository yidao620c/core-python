#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 双向队列
"""
from collections import deque

dq = deque(range(10), maxlen=10)
dq.rotate(3)  # 向前滚动3格
print(dq)
dq.rotate(-4)  # 向后滚动4格
print(dq)
dq.appendleft(-1)  # 左边添加元素-1
print(dq)
dq.extend([11, 22, 33])  # 右边扩充队列
print(dq)
dq.extendleft([10, 20, 30, 40])  # 左边扩充队列
print(dq)
