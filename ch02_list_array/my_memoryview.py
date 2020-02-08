#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 内存视图
"""
import array
numbers = array.array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))
memv_oct = memv.cast('B')
print(memv_oct.tolist())
memv_oct[5] = 4
print(numbers)

