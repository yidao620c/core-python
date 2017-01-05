#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Desc: something
"""
__author__ = "Xiong Neng"

import samples.main

samples.main.cc()

class A:
    def _a(self):
        print('_a')
    def __aa(self):
        print('__aaa')

if __name__ == '__main__':
    main_module = __import__('samples.main')
    main_module.ttt = "tttttt"
    import samples.main

    pass