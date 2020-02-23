#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: @contextmanager装饰器

在使用 @contextmanager 装饰的生成器中，yield 语句的作用是把函数的定义体分成两
部分：yield 语句前面的所有代码在 with 块开始时（即解释器调用 __enter__ 方法
时）执行， yield 语句后面的代码在 with 块结束时（即调用 __exit__ 方法时）执行。
"""

import contextlib


@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    try:
        yield 'JABBERWOCKY'  # 分水岭，yield前面是调用 __enter__ 方法时候执行，并将yield结果赋值给as
    except ZeroDivisionError:
        msg = 'Please DO NOT divide by zero!'
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)
