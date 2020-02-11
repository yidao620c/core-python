#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 使用 __slots__ 类属性节省空间

__slots__不会继承，Python 只会使用各个类中定义的__slots__ 属性，它是一个类属性，类属性是不会继承的。
"""


class A:
    typecode = 'd'

    def __init__(self, a, b):
        self.a = a
        self.b = b + self.typecode


class B(A):
    def __init__(self, b, c):
        super().__init__(b, c)

    def test(self, t, h):
        print(A.typecode)
        print(self.a)
        print(self.b)


B(4, 5).test(20, 20)


class Vector2d:
    # Python 会在各个实例中使用类似元组的结构存储实例变量，从而避免使用消
    # 耗内存的 __dict__ 属性。
    __slots__ = ('__x', '__y')
    typecode = 'd'
