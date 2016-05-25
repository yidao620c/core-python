#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 七牛上传图片并
Desc : 
"""

from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config
import os
from os.path import join
import sys

if __name__ == '__main__':
    # 需要填写你的 Access Key 和 Secret Key
    access_key = 'wwnxKGHKqnYMLnZbaIPc-ejWZH1MGIqGrRQaHaef'
    secret_key = 'EFdx312y3RA6c9iVTS-gj3oPthkKpKNudmtRoECg'

    url_pre = 'http://yidaospace.qiniudn.com/'

    # 构建鉴权对象
    q = Auth(access_key, secret_key)

    # 要上传的空间
    bucket_name = 'yidaospace'
    current_dir = os.path.dirname(os.path.realpath(__file__))
    pfs = [f for f in os.listdir(current_dir)
           if os.path.isfile(join(current_dir, f))
           and not f.endswith('url.txt') and not f.endswith('qiniuniu.py')]
    urls = []
    for f in pfs:
        localfile = join(current_dir, f)
        if os.path.isfile(localfile) and f != 'url.txt':
            # 上传到七牛后保存的文件名
            key = f
            # 生成上传 Token，可以指定过期时间等
            token = q.upload_token(bucket_name, key, 3600)
            # 要上传文件的本地路径
            ret, info = put_file(token, key, localfile)
            # 上传完后删除文件
            os.remove(localfile)
            # 将url写入文本
            urls += url_pre + f + '\n'

    with open(os.path.join(current_dir, 'url.txt'), 'a', encoding='utf-8') as uf:
        uf.writelines(urls)
