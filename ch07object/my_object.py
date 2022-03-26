#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: sample
Desc : 
"""


class Phone(object):
    def __init__(self, brand, model, weight, color):
        self.__brand = brand
        self.__model = model
        self.__weight = weight
        self.__color = color

    def print_color(self):
        print('color is {}'.format(self.__color))

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

phone = Phone('Huawei', 'P30', '174.00g', '幻影蓝')
# print(phone.__color)  # cannot access
phone.print_color()

