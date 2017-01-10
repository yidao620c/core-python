#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    Topic: sample
    Desc : 
"""
import sys, os

__author__ = 'Xiong Neng'


class User(object):
    def __init__(self, name):
        self.name = name


def aa():
    for x in range(1, 10):
        for y in range(1, x + 2):
            yield '%d * %d = %d\t' % (y, x, x * y) if y <= x else '\n'
            print('ddd')


b = 1


def bb():
    a = b + 2
    print(a)


def cc():
    print(__name__)
    pass


if __name__ == '__main__':
    a = 1
    bb()

    disklist = [{'wwid': '111', 'name': '11112'},
                {'wwid': '222', 'name': '2222'},
                {'wwid': '333', 'name': '3332'},
                {'wwid': '444', 'name': '4442'}]

    all_wwiddisk_list = [{'wwid': '111', 'name': '11112'},
                         {'wwid': '555', 'name': '5552'},
                         {'wwid': '666', 'name': '6662'}]

    kk = (db_disk['wwid'] for db_disk in disklist)
    print(kk)

    print([dd for dd in all_wwiddisk_list if dd['wwid'] not in (db_disk['wwid'] for db_disk in disklist)])

    if '1' in ('1', '2'):
        print('OK')

    zz = (1, 2)
    print(type(zz))

    zz = {}
    print(type(zz))

    zz = ()
    print(type(zz))
