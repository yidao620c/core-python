#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 字符编码解码
"""

s = 'café'
print('s.type={}, s.len={}'.format(type(s), len(s)))
b = s.encode('utf8')
print('b={}'.format(b))
print('type={}'.format(type(b)))
print('b.len={}'.format(len(b)))
ss = b.decode('utf8')
print(ss)
