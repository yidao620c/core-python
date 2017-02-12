#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

:copyright: (c) 2017 by Xiong Neng.
:license: MIT, see LICENSE for more details.
"""

import hashlib
import os

def md5hex(word):
    """ MD5加密算法，返回32位小写16进制符号"""
    if not isinstance(word, str):
        word = str(word)
    m = hashlib.md5()
    m.update(word)
    return m.hexdigest()


def md5sum(fname):
    """ 计算文件的MD5值"""
    def read_chunks(fh):
        fh.seek(0)
        chunk = fh.read(8096)
        while chunk:
            yield chunk
            chunk = fh.read(8096)
        else:  # 最后要将游标放回文件开头
            fh.seek(0)

    m = hashlib.md5()
    if isinstance(fname, str) and os.path.isfile(fname):
        with open(fname, "rb") as fh:
            for ck in read_chunks(fh):
                m.update(ck)
    else:
        return ""

    return m.hexdigest()

