#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: sample
Desc : 
"""

from functools import reduce
from typing import Iterable, Iterator


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(int, s))


print(str2int('54321'))

print(reduce(lambda x, y: x + y, (x for x in range(10))))

print(list(filter(lambda x: x % 2 == 1, range(0, 11))))
print(list(filter(lambda x: x != ':', ['a', 'b', ':', 'c', ':', '!'])))

print(sorted((2, 1, 5, 3, 4), reverse=True))

d = {'zhangsan': -22, 'lisi': 13, 'wangwu:': 16}
print(sorted(d.items(), key=lambda item: abs(item[1])))

l = [1, 2, 3, 4, 5]
new_list = map(lambda x: x * 2, l)
print(isinstance(new_list, Iterable))
print(isinstance(new_list, Iterator))

