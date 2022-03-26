#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 注册虚拟子类
"""

from random import randrange

from ch07object.my_abc_class import Tombola


class TomboList(list):
    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))


issubclass(TomboList, Tombola)
t = TomboList(range(100))
isinstance(t, Tombola)

