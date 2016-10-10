#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: sample
Desc : 
"""

import sys

def get_cur_info():
    print(sys._getframe().f_code.co_filename)  #当前文件名，可以通过__file__获得
    print(sys._getframe(0).f_code.co_name)  #当前函数名
    print(sys._getframe(1).f_code.co_name) #调用该函数的函数的名字，如果没有被调用，则返回<module>，貌似call stack的栈低
    print(sys._getframe().f_lineno) #当前行号
    print(sys._getframe(1).f_globals)


import codecs
import datetime
filename = "D:/temp/zz.log"
def _write_log(msg):
    nowtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with codecs.open(filename, "a", encoding='utf-8') as myfile:
        myfile.write("%s: %s\n" % (nowtime, msg))


if __name__ == '__main__':
    aa = {'1', '2', '3'}
    disks_db = [{'device_name': '1', 'ddd': 'dd'}]
    exists_disks = set(d['device_name'] for d in disks_db)
    print(aa - exists_disks)


