#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: sample
Desc : 
"""

_list = ['a', 'b', 'c', 'd', 'e']

sub_list = _list[-1::-2]

print(sub_list)

_tuple = ('a', 'b', 'c', 'd', 'e')
sub_tuple = _tuple[-1::-2]
_str = 'abcde'
sub_str = _str[-1::-2]
print(sub_tuple)
print(sub_str)

print("\n".join("\t".join(["%s * %s = %s"%(y, x, x*y) for y in range(1, x+1)]) for x in range(1, 10)))

_list = [x for x in range(6)]
print(_list)

_list_generator = (x for x in range(6))
print(_list_generator)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    yield 'done'


_list_generator = (x for x in range(3))
print(next(_list_generator))
print(next(_list_generator))
print(next(_list_generator))
print(next(_list_generator))
