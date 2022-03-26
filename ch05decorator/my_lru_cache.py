#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: functools.lru_cache做备忘
被 lru_cache 装饰的函数，它的所有参数都必须是可散列的。
"""
import functools

from ch05decorator.my_time_decorator import clock


@functools.lru_cache()
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == '__main__':
    print(fibonacci(6))
