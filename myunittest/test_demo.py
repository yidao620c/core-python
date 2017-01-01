#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
推荐运行方式为 python3 -m unittest test_demo
"""
__author__ = "Xiong Neng"

import unittest

class TestDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        "Hook method for setting up class fixture before running tests in the class."
        pass

    @classmethod
    def tearDownClass(cls):
        "Hook method for deconstructing the class fixture after running all tests in the class."
        pass

    def setUp(self):
        "Hook method for setting up the test fixture before exercising it."
        pass

    def tearDown(self):
        "Hook method for deconstructing the test fixture after testing it."
        pass

    def test_a(self):
        d = {}
        with self.assertRaises(KeyError):
            value = d['ddd']
    def test_b(self):
        d = {}
        with self.assertRaises(AttributeError):
            value = d.dd


# mydict2.py
class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__=='__main__':
    # 演示下文档测试
    import doctest
    doctest.testmod()