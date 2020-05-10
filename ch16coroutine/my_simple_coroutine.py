#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: sample
"""


def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received x:', x)


if __name__ == '__main__':
    # my_coro = simple_coroutine()
    # print('------------------')
    # print(my_coro)  # 生成器对象
    # next(my_coro)  # next函数启动生成器，并在yield语句停住。my_coro.send(None)，效果一样
    # print('------------------')
    # my_coro.send(55)

    print(type({}))

