#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 闭包示例
只有嵌套在其他函数中的函数才可能需要处理不在全局作用域中的外部变量。
"""


def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)  # 这里series是自由变量
        total = sum(series)
        return total / len(series)

    return averager


avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))

print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)
print(avg.__closure__)
print(avg.__closure__[0].cell_contents)
