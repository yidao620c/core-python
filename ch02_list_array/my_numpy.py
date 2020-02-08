#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: Numpy简单演示
"""
import numpy

a = numpy.arange(12)
print(a)
print(type(a))
print(a.shape)
a.shape = 3, 4
print(a)
print(a[:, 1])
print(a.transpose())


