#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 不可修改字典，相当于字典视图。
"""

from types import MappingProxyType

d = {1:'A'}
d_proxy = MappingProxyType(d)
print(d_proxy[1])
# 不可对d_proxy做修改操作，但是对于底层的d修改后可反映到视图上来。

