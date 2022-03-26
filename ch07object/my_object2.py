#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: sample
Desc : 
"""

class Phone(object):

    weight = 20  # 类属性

    def __init__(self, brand, color):
        self.__brand = brand
        self.__color = color

    def print_color(self):
        print('color is {}'.format(self.__color))
        return self.__color


class SmartPhone(Phone):
    def __init__(self, brand, color, touch_screen):
        super().__init__(brand, color)
        self.__touch_screen = touch_screen

    def print_color(self):
        print('[SmartPhone] {}'.format(super().print_color()))

    def print_touch_screen(self):
        print('touch_screen is {}'.format(self.__touch_screen))


if __name__ == '__main__':
    p = SmartPhone('brand', 'blue', '电容屏')
    p.print_color()

    print(isinstance(p, SmartPhone))
    print(isinstance(p, Phone))

    print(type(p))
    print(type(123))
    print(type('test'))
    print(type(None))
    print(type(type(123)))

    import types
    def fn():
        pass

    print(type(fn) == types.FunctionType)
    print(type(abs) == types.BuiltinFunctionType)
    print(type(lambda x: x) == types.LambdaType)
    print(type((x for x in range(10))) == types.GeneratorType)

    print(dir('test'))

    print(hasattr(p, 'name'))
    print(hasattr(p, '__touch_screen'))  # 双下划线开头的私有属性获取不到
    print(hasattr('test', 'isupper'))
    print(getattr('test', 'lower'))
    setattr(p, 'name', 'ZJJ') # 设置一个属性'name'
    print(getattr(p, 'name', 'nothing')) #还能传入一个默认值，如果属性不存在则返回默认值
    print(SmartPhone.weight)
    print(p.weight)
