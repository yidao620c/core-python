#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 算术运算符模块operator
"""

from functools import reduce
from operator import mul


def fact(n):
    """计算阶乘"""
    return reduce(mul, range(1, n + 1))


from operator import itemgetter

metro_data = [('Tokyo', 'JP', 36.933, (35.689722, 139.691667))]
# itemgetter 使用 [] 运算符，因此它不仅支持序列，还支持映射和任何实现__getitem__方法的类。
for city in sorted(metro_data, key=itemgetter(1)):  # 按照每个元组第2个元素排序
    print(city)

from collections import namedtuple
from operator import attrgetter

LatLong = namedtuple('LatLong', 'lat long')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')
metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long))
               for name, cc, pop, (lat, long) in metro_data]
print(metro_areas[0])
name_lat = attrgetter('name', 'coord.lat')
for city in sorted(metro_areas, key=attrgetter('coord.lat')):
    print(name_lat(city))
