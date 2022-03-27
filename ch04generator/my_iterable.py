# -*- encoding: utf-8 -*-
"""
description
"""
from typing import Iterable, Iterator, Generator


class MyIter:
    def __iter__(self):
        yield 3


print(isinstance(MyIter(), Iterable))
print(isinstance(MyIter.__iter__, Generator))
print(isinstance(MyIter().__iter__, Iterator))
print(isinstance(MyIter().__iter__(), Generator))
print(isinstance(MyIter().__iter__(), Iterator))
print(isinstance(iter(MyIter()), Iterator))


def my_iter():
    for i in range(10):
        print(f'-------------{i}')
        yield i


iter_func = my_iter()
print(5 in iter_func)
print(8 in iter_func)
print(99 in iter_func)
