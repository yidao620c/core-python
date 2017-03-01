#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
字符串相关帮助类
:copyright: (c) 2017 by Xiong Neng.
:license: MIT, see LICENSE for more details.
"""
import random
import string

def random_alpha(n):
    """How do I generate a random string (of length n, a-z only) """
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(n))


if __name__ == '__main__':
    print(random_alpha(8))