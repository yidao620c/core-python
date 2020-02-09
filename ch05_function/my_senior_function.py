#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 高阶函数：将函数当成参数或返回值
"""

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']


def reverse(word):
    return word[::-1]


reverse('testing')
print(sorted(fruits, key=reverse))

