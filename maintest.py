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
    pass
