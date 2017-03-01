#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Desc: something
"""
import collections
from collections import defaultdict
import fileinput
import itertools

db_pool_listd = [(1,2), (3,), (4,5)]
db_pool_list = itertools.chain.from_iterable(db_pool_listd)
print(list(db_pool_list))

import json, ast
# r = {u'name': u'A', u'primary_key': 1}
# a = json.loads(json.dumps(ast.literal_eval('')))

a = {}
b = ()
c = []
d = set()
print(type(a), type(b), type(c), type(d))

class A():
    pass

a = {(1, A()) : [1, [2, 3,3]]}
for k,v in a.items():
    print(k[0], '---', k[1])
    print(v)

print(float('12.99'), float(11), float(23.99))

print('{:.2f}'.format(12.635))
print('{:.2f}'.format(12.645))
print('{:.2f}'.format(2.645))

import decimal
decimal.getcontext().rounding = decimal.ROUND_UP
print('{:.2f}'.format(decimal.Decimal(12.645)))
print('{:.2f}'.format(decimal.Decimal(2.645)))

a = (1, 2, 3, 4)
s, ss, *abc = a
print(ss, s)
print(type(abc))

import random,string
def random_alpha(size):
    """How do I generate a random string (of length X, a-z only) """
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(size))


print(random_alpha(3))

