#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: sample
Desc : 
"""

b = 6


def test(a):
    print(a)
    global b
    print(b)  # 当函数执行到这一步会报错
    # UnboundLocalError: local variable 'b' referenced before assignment
    b = 9  # 比示例二多了一行赋值


test(1)


def get_avg():
    scores = 0  # 将外部临时变量由 list 改为一个 整型数值
    count = 0  # 同时新增一个变量，记录个数

    def inner_count_avg(val):  # 内部函数，用于计算平均值
        nonlocal scores, count
        scores += val  # 使用外部函数的临时变量
        count += 1
        return scores / count  # 返回计算出的平均值

    return inner_count_avg  # 外部函数返回内部函数引用


avg = get_avg()
print(avg(10))
print(avg(11))
