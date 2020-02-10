#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 不要使用可变类型作为参数的默认值。

出现这个问题的根源是，默认值在定义函数时计算（通常在加载模块时），因此默认值变成了函数对象的属性。
对象的方法也是函数对象，def定义的都是函数对象。
"""


class HauntedBus:
    """备受幽灵乘客折磨的校车"""

    def __init__(self, passengers=[]):
        self._passengers = passengers

    def pick(self, name):
        self._passengers.append(name)

    def drop(self, name):
        self._passengers.remove(name)


bus1 = HauntedBus(['Alice', 'Bill'])
print(bus1._passengers)
bus1.pick('Charlie')
bus1.drop('Alice')
print(bus1._passengers)
bus2 = HauntedBus()
bus2.pick('Carrie')
print(bus2._passengers)
bus3 = HauntedBus()
print(bus3._passengers)
bus3.pick('Dave')
print(bus2._passengers)
print(bus2._passengers is bus3._passengers)
print(bus1._passengers)
print(type(HauntedBus.drop))  # <class 'function'>
print(type(bus1.drop))  # <class 'method'>
print(dir(HauntedBus.__init__))
print(HauntedBus.__init__.__defaults__)
print(HauntedBus.__init__.__defaults__[0] is bus2._passengers)


