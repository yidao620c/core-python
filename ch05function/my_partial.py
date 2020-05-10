#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 闭包，冻结部分参数
functools.partial 这个高阶函数用于部分应用一个函数。部分应用是指，基于一个函
数创建一个新的可调用对象，把原函数的某些参数固定。
"""

from functools import partial
from operator import mul

triple = partial(mul, 3)
print(triple(7))
print(list(map(triple, range(1, 10))))
