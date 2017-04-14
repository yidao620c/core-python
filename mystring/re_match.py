#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
desc: regex match demo

:copyright: (c) 2017 by Xiong Neng.
:license: MIT, see LICENSE for more details.
"""
import re

if __name__ == '__main__':
    """main test"""
    # 匹配小数(1, 1.0, 0.22)，不匹配1.，.3
    patt = re.compile(r'^\d+(\.(?=\d+)\d+)?$')
    print(patt.match('1.045'))
    print(patt.match('1'))
    print(patt.match('0.22'))
    print(patt.match('1.'))
    print(patt.match('.3'))

    # 不捕获括号分组用法
    size_pt = re.compile(r'^(\d+(?:\.(?=\d+)\d+)?)(\D+)$')
    print(size_pt.match('3.8GB').group(1))
    print(size_pt.match('3.8GB').group(2))

    # print(patt.match('1.').group(0))

