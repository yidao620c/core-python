#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: sample
"""

def gen_ab():
    print('start')
    yield '111'
    print('continue')
    yield '222'
    print('end')


a = gen_ab()
print('------------------')
print(next(a))
