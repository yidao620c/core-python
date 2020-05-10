#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 字符串比较的时候先标准化
保存文本之前，最好使用 normalize('NFC', user_text) 清洗字符串
不区分大小写的比较应该使用 str.casefold()
"""

from unicodedata import normalize

s1 = 'café'  # 把"e"和重音符组合在一起
s2 = 'cafe\u0301'  # 分解成"e"和重音符
print(len(s1), len(s2))
print(len(normalize('NFC', s1)), len(normalize('NFC', s2)))
print(len(normalize('NFD', s1)), len(normalize('NFD', s2)))
print(normalize('NFC', s1) == normalize('NFC', s2))
print(normalize('NFD', s1) == normalize('NFD', s2))
