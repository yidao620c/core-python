#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: main测试类
Desc : 
"""
import collections

if __name__ == '__main__':
    VmdkInfo = collections.namedtuple('VmdkInfo', ['path', 'adapter_type',
                                               'disk_type',
                                               'capacity_in_bytes',
                                               'device'])
    a = VmdkInfo('d', 'dd', 'dd',
                        None, None)
    print(a.path)
    pass


    print(chr(ord('a') + 2))
    hostid_prefix= 'node'
    i = 4
    print("{}{:04d}".format(hostid_prefix, i + 1))

    print('mon.{}'.format(chr(ord('a') + 4)))

