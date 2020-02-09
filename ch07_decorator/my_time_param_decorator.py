#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 带参数的计时器装饰器
"""

import functools
import time

DEFAULT_FMT = '[{:0.8f}s] {}({}) -> {}'


def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        @functools.wraps(func)
        def clocked(*args, **kwargs):
            t0 = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - t0
            name = func.__name__
            arg_str = ', '.join(repr(arg) for arg in args)
            print(DEFAULT_FMT.format(elapsed, name, arg_str, repr(result)))
            return result

        return clocked

    return decorate


@clock()
def snooze(seconds):
    time.sleep(seconds)


if __name__ == '__main__':
    for i in range(3):
        snooze(.123)
    d = {'name': 'zhangsan', 'age': 12}
    print('name={name}'.format(**d))