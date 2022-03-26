#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 字典映射
"""
import collections

DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]

country_code = {country: code for code, country in DIAL_CODES}
print(country_code)

"""创建从一个单词到其出现情况的映射"""
import re
import sys

WORD_RE = re.compile(r'\w+')
index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
column_no = match.start() + 1
location = (line_no, column_no)
index.setdefault(word, []).append(location)
# 以字母顺序打印出结果
for word in sorted(index, key=str.upper):
    print(word, index[word])

# Counter计数器
ct = collections.Counter('abracadabra')
ct.update('aaaaazzz')
print(ct.most_common(2))


class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item
