#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 对象弱引用

弱引用不会增加对象的引用数量。引用的目标对象称为所指对象（referent）。因此我们
说，弱引用不会妨碍所指对象被当作垃圾回收。
"""

import weakref
a_set = {0, 1}
wref = weakref.ref(a_set)
print(wref)
print(wref()) # 弱引用是可调用的对象，调用后返回的是被引用的对象；如果所指对象不存在了，返回 None
a_set = {2, 3, 4}
print(wref())
print(wref() is None)
print(wref() is None)

class Cheese:
    def __init__(self, kind):
        self.kind = kind
    def __repr__(self):
        return 'Cheese(%r)' % self.kind

stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'),Cheese('Brie'), Cheese('Parmesan')]
for cheese in catalog:
    stock[cheese.kind] = cheese
print(sorted(stock.keys()))
del catalog
print(sorted(stock.keys()))
del cheese
print(sorted(stock.keys()))
