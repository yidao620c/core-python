#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: sample
"""


from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print('{},{},{}'.format(tokyo.population, tokyo.name, tokyo.country))

# 类属性
print(City._fields)
