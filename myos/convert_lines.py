#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Topic: sample
Desc : 
"""

def str2int(s):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


if __name__ == '__main__':
    import sys, os
    def convert(orig):
        with open(orig) as f:
            lines = f.readlines()
        new_name = os.path.join(os.path.dirname(os.path.realpath(orig)),
                                '{}_result.txt'.format(os.path.basename(os.path.splitext(orig)[0])))
        with open(new_name, 'w') as f:
            f.writelines(['{}-{}-{}-{}-{}'.format(s[:8], s[8: 12], s[12:16], s[16:20], s[20:]).upper() for s in lines])
    if sys.argv[1].endswith('.txt'):
        convert(sys.argv[1])
    else:
        for file in [f for f in os.listdir(sys.argv[1]) if f.endswith('.txt')]:
            convert(os.path.join(sys.argv[1], file))