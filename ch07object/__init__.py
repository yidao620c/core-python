#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 对象引用、可变性和垃圾回收
"""

a = [1, 2, 3]
print(id(a))
a += [5, 6]  # 如果是可变类型，+=就地修改内容，不改变引用地址，不创建新对象。
print(id(a))

b = (1, 2)
print(id(b))
bb = b[:]
print(id(bb))
print(b is bb)
