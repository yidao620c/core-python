#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 生成器表达式
"""

# 用生成器表达式初始化元组和数组
symbols = '$¢£¥€¤'
t1 = tuple(ord(symbol) for symbol in symbols)
print(t1)

import array
a1 = array.array('I', (ord(symbol) for symbol in symbols))
print(a1)


