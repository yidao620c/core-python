#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 二进制序列类型bytes和bytearray

bytes是不可变的二进制序列，而bytearray是可变二进制序列
"""

if __name__ == '__main__':
    a = b"abc"
    aa = bytearray(a)
    aa.append(49)
    print(aa)
    pass


def test():
    cafe = bytes('café', encoding='utf_8')  # 各个元素是 range(256) 内的整数
    print('cafe.type={}, cafe.value={}'.format(type(cafe), cafe))
    print('cafe[0].type={}, cafe[0].value={}'.format(type(cafe[0]), cafe[0]))
    print('cafe[:1].type={}, cafe[:1].value={}'.format(type(cafe[:1]), cafe[:1]))

    cafe_arr = bytearray(cafe)
    print(cafe_arr, cafe_arr[-1:])

    bb = bytes.fromhex('31 4B CE A9')
    print(bb)
