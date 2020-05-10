#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 继承与抽象基类

协议是约定的接口，不是正式的接口。
抽象基类对接口一致性的强制
"""
from typing import Iterable


class A:
    pass
    # def __iter__(self):
    #     return None

a = A()
print(isinstance(a, Iterable))

