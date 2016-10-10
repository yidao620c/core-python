#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: main测试类
Desc : 
"""
from functools import reduce
from mystring import xunicode
from enum import IntEnum

class State(IntEnum):
    """
    NOT_INITIALIZED 0 INITIALIZE_ALL_COMPLETE 是最后一步，作为一个最大的整数。
    """
    NOT_INITIALIZED = 0

    INITIALIZE_NETWORK_COMPLETE = 1
    INITIALIZE_CONF_COMPLETE = 2
    INITIALIZE_SSD_COMPLETE = 3
    INITIALIZE_MON_COMPLETE = 4
    INITIALIZE_OSD_COMPLETE = 5
    INITIALIZE_CLUSTER_COMPLETE = 6
    INITIALIZE_WINSTORE_SERVICE_COMPLETE = 7
    INITIALIZE_WINSTORE_MASTER_COMPLETE = 8

    INITIALIZE_ALL_COMPLETE = 9


def str2int(s):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


if __name__ == '__main__':
    # print(str2int('34243'))
    # print(list(filter(lambda n: n % 2 == 1, [1, 2, 4, 5, 6, 9, 10, 15])))
    # print(sorted([36, 5, -12, 9, -21], key=abs))
    # print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
    # print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
    # a = xunicode.sub(r'(foo)(bar)', r'\g<1>123\g<2>', 'foobar')
    # state = State['INITIALIZE_CLUSTER_COMPLETE']
    # print(int(100 * state / State["INITIALIZE_ALL_COMPLETE"].value))
    pass

def aa(a, b=2):
    print(aa.__dict__)
    pass

aa(1,1)
aa.__dict__['1'] = '2'
aa(1,1)