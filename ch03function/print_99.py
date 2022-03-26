#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 一句话打印九九乘法表
Desc : 
"""

print("\n".join("\t".join(["{} * {} = {}".format(y, x, x*y) for y in range(1, x+1)]) for x in range(1, 10)))

