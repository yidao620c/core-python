#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
能返回结果的coroutine
"""
from collections import namedtuple

Result = namedtuple("Result", "count average")

def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        val = yield
        if val is None:
            break
        count +=1
        total += val
        average = total / count
    return Result(count, average)

if __name__ == '__main__':
    coro_avg = averager()
    next(coro_avg)
    coro_avg.send(10)
    coro_avg.send(30)
    coro_avg.send(6.5)
    try:
        coro_avg.send(None)
    except StopIteration as exc:
        result = exc.value

    print(result)

