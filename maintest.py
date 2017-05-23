#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: main测试类
Desc : 
"""
import collections
import traceback

log_dict = {
    'winstore.common': '/opt/winstore/var/log/winstore/common.log',
    'winstore.api': '/opt/winstore/var/log/winstore/api.log',
    'winstore.agent': '/opt/winstore/var/log/winstore/agent.log',
    'winstore.agent.system': '/opt/winstore/var/log/winstore/system.log',
    'winstore.db': '/opt/winstore/var/log/winstore/db.log',
}


def _get_key(module_name):
    """根据模块名获取日志key"""
    mlist = module_name.split('.')
    mlen = len(mlist)
    while mlen > 1:
        cutkey = '.'.join(mlist[:mlen])
        if cutkey in log_dict:
            return cutkey
        mlen -= 1
    return "default"

if __name__ == '__main__':
    """test"""
    from datetime import datetime
    print(datetime.now())

    print('\'' + '222' + '\'')
