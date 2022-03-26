#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 枚举类
Desc : 
"""

from enum import Enum, unique


@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


for name, member in Weekday.__members__.items():
    print(name, '=>', member, ',', member.value)
