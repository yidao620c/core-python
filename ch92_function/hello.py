#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: sample
Desc : 
"""


def hello(name):
    """
    hello world
    """
    print('hello world, ' + name)


def multi_result(a, b, c):
    return a + 1, b + 1, c + 1

r = multi_result(1, 2, 3)
print(r)

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
param={'city': 'XiAn', 'job': 'Engineer'}
person('name', 24, **param)

def person(name, age, *args, city, job):
    print(name, age, args, city, job)
