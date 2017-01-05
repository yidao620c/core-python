#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
set集合操作
"""
__author__ = "Xiong Neng"

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruit = set(basket)

a = set('abracadabra')
b = set('alacazam')

# 或
print(a.union(b))
print(a | b)

# 与
print(a.intersection(b))
print(a & b)

# 差
print(a.difference(b))
print(a - b)

# 异或
print(a.symmetric_difference(b))
print(a ^ b)

# 成员in
print('a' in a)
print('z' not in a)

# 子集
s = set('acada')
print(s.issubset(a))

# 超集
print(a.issuperset(s))

# 或更新
a.update(b)
a |= b

# 与更新
a.intersection_update(b)
a &= b

# 差更新
a.difference_update(b)
a -= b

# 异或更新
a.symmetric_difference_update(b)
a ^= b

# 增加
a.add(b)

# 删除
a.remove(b)   # 如果不存在则引发 KeyError
a.discard(b)  # 如果不存在没事

# 清空
a.clear()



