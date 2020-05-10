#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic:
for-else：正常执行完才会执行else，也就是没有执行过return、break
while-else：正常执行完才会执行else，也就是没有执行过return、break
try-else：正常执行完才会执行else，也就是没有抛异常。
"""

items = [1, 2, 3]

for i in items:
    if i == 2:
        continue
    print(i)
else:
    print('for else')

i = 0
while i < len(items):
    i += 1
    if i == 2:
        break
    print(items[i-1])
else:
    print('while else')