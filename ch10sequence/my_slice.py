#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 切片原理
"""


class MySeq:
    def __getitem__(self, index):
        return index


s = MySeq()
print(s[1])
print(s[1:4])
print(s[1:4:2])
print(s[1:4:2, 9])
print(s[1:4:2, 7:9])

print(slice(-3, 0, -1).indices(5))
