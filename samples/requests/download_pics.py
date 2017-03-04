#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
desc: 下载七牛上面所有图片

:copyright: (c) 2017 by Xiong Neng.
:license: MIT, see LICENSE for more details.
"""
import requests
import re
import os

def down_allpic(crush_file):
    urls = []
    id_pattern = re.compile(r' data-clipboard-text="(.*?)"', re.MULTILINE)
    with open(crush_file, encoding='utf-8') as f:
        content = f.read()
    for m in id_pattern.finditer(content):
        urls.append(m.group(1))
    print(len(urls))
    down_dir = r'D:/download/20170304/'
    for u in urls:
        if (u.endswith('.zip') or u.endswith('/')):
            continue
        print(u)
        # 直接返回原始的内容
        r = requests.get(u, stream=True)
        # 然后使用字节流下载对应的内容
        chunk_size = 1024
        with open(os.path.join(down_dir, os.path.split(u)[1]), 'wb') as fd:
            for chunk in r.iter_content(chunk_size):
                fd.write(chunk)
    return urls


if __name__ == '__main__':
    down_allpic(r'D:/work/projects/gitprojects/core-python/zzz.txt')
