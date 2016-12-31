#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Desc: OOP一些小例子
"""
__author__ = "Xiong Neng"


def tt():
    pass


if __name__ == '__main__':
    print(type(123) == int)
    print(type('123') == str)
    # 断基本数据类型可以直接写int，str等，
    # 但如果要判断一个对象是否是函数怎么办？
    # 可以使用types模块中定义的常量：
    import types
    print(type(tt) == types.FunctionType)
    print(type(abs) == types.BuiltinFunctionType)
    print(type(lambda x: x) == types.LambdaType)
    print(type((x for x in range(10))) == types.GeneratorType)

    class Student(object):
        pass

    # 给实例绑定方法，对其他实例不起作用
    s = Student()
    def set_age(self, age):
        self.age = age
    from types import MethodType
    s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
    s.set_age(25) # 调用实例方法
    print(s.age)  # 测试结果

    # 为了给所有实例都绑定方法，可以给class绑定方法：
    def set_score(self, score):
        self.score = score
    Student.set_score = set_score
    s.set_score(333)
    print(s.score)

    # 通常情况下，上面的set_score方法可以直接定义在class中，
    # 但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。

    # 使用__slots__
    # __slots__变量，来限制该class实例能添加的属性
    class Student(object):
        __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
    s = Student() # 创建新的实例
    # s.score = 99 # 绑定属性'score' 出错了...
    # 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
    # 除非在子类中也定义__slots__，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__


    # @property
    # 有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？
    # 对于追求完美的Python程序员来说，这是必须要做到的！
    class Student(object):
        @property
        def scoreddd(self):
            return self._score

        @scoreddd.setter
        def scoreddd(self, value):
            if not isinstance(value, int):
                raise ValueError('score must be an integer!')
            if value < 0 or value > 100:
                raise ValueError('score must between 0 ~ 100!')
            self._score = value
    # @property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，
    # 只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，
    # 负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：


    # __iter__和__getitem__的使用
    class Fib(object):
        def __init__(self):
            self.a, self.b = 0, 1 # 初始化两个计数器a，b

        def __iter__(self):
            return self # 实例本身就是可迭代对象，故返回自己

        def __next__(self):
            self.a, self.b = self.b, self.a + self.b # 计算下一个值
            if self.a > 100000: # 退出循环的条件
                raise StopIteration();
            return self.a # 返回下一个值

        def __getitem__(self, n):
            if isinstance(n, int): # n是索引
                a, b = 1, 1
                for x in range(n):
                    a, b = b, a + b
                return a
            if isinstance(n, slice): # n是切片
                start = n.start
                stop = n.stop
                if start is None:
                    start = 0
                a, b = 1, 1
                L = []
                for x in range(stop):
                    if x >= start:
                        L.append(a)
                    a, b = b, a + b
                return L

    # __getattr__()的使用
    # 注意，只有在没有找到属性的情况下，才调用__getattr__，
    # 已有的属性，比如name，不会在__getattr__中查找
    # 这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
    def __getattr__(self, attr):
        if attr=='score':
            return 99
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

    from enum import Enum, unique
    Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                           'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
    for name, member in Month.__members__.items():
        print(name, '=>', member, ',', member.value)
    @unique
    class Weekday(Enum):
        Sun = 0 # Sun的value被设定为0
        Mon = 1
        Tue = 2
        Wed = 3
        Thu = 4
        Fri = 5
        Sat = 6
    day1 = Weekday.Mon
    print(day1 == Weekday.Mon)