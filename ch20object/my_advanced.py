#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: sample
Desc : 
"""


#
# class Phone(object):
#     pass
#
#
# p = Phone()
# p.name = 'Xiong Neng'  # 绑定属性
# print(p.name)
#
#
# def set_age(self, age):  # 定义一个函数作为实例方法
#     self.age = age
#
#
# from types import MethodType
#
# p.set_age = MethodType(set_age, p)  # 给实例绑定一个方法
# p.set_age(25)  # 调用实例方法
# print(p.age)  # 测试结果
#
#
# class Phone(object):
#     __slots__ = ('brand', 'color')  # 用tuple定义允许绑定的属性名称


# p = Phone()
# p.name = 'Xiong Neng'  # 绑定属性
# print(p.name)


class Phone(object):
    def __init__(self, brand, color):
        self._brand = brand
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if not isinstance(value, str):
            raise ValueError('color must be an string!')
        if value not in ('red', 'blue', 'white'):
            raise ValueError('score must be one of red, blue, white!')
        self._color = value


p = Phone('brand', 'red')
p.color = 'blue'
