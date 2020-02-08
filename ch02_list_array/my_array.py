#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 数组
"""

from array import array
from random import random


def f1():
    global fp
    floats = array('d', (random() for i in range(10 ** 5)))
    print(floats[-1])
    fp = open('floats.bin', 'wb')
    floats.tofile(fp)
    fp.close()


def f2():
    global fp
    floats2 = array('d')
    fp = open('floats.bin', 'rb')
    floats2.fromfile(fp, 10 ** 5)
    fp.close()
    print(floats2[-1])


if __name__ == '__main__':
    f2()
