#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 自省
"""

# 列出常规对象没有而函数有的属性
class C: pass
obj = C()
def func(): pass
print(sorted(set(dir(func)) - set(dir(obj))))


