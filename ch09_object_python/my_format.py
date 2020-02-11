#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 格式化输出
"""

brl = 1/2.43
print(brl)
print(format(brl, '0.4f'))
print('1 BRL = {rate:0.2f} USD'.format(rate=brl))
print(format(42, 'b'))
print(format(2/3, '.1%'))

