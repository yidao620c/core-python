#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    Topic: sample
    Desc : 输出python是32位还是64位
"""
import struct

__author__ = 'Xiong Neng'

print(u'%d位' % (struct.calcsize("P") * 8,))

import platform
print(platform.python_version())

print("dd" + "333")

ssd_osds = None

a = [ item[0] for item in ssd_osds] if ssd_osds else None

