#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: main测试类
Desc : 
"""
import os
import re


if __name__ == '__main__':
    print("CLICKS{:d}".format(111))
    print('CLICKS111'[6:])

    print(list([2]))
    try:
        import multiprocessing  # noqa
    except ImportError:
        print('dd')
        pass

