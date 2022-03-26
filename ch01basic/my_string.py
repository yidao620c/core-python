#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 字符串编码解码
"""

if __name__ == '__main__':
    s = "汉子"
    print(len(s))
    print(type('汉'))
    print(ord("汉"))  # code point
    print(hex(ord('汉')))  # code point
    print(chr(0x6c49))
    # 字符串字面量literal支持八进制、十六进制、Unicode编码
    # Unicode格式小写\u表示16位整数，大写\U表示32位整数编码格式。
    print('H\x69, \u6c49\U00005B57')
    pass


def test():
    s = 'café'
    print('s.type={}, s.len={}'.format(type(s), len(s)))
    b = s.encode('utf8')
    print('b={}'.format(b))
    print('type={}'.format(type(b)))
    print('b.len={}'.format(len(b)))
    ss = b.decode('utf8')
    print(ss)
