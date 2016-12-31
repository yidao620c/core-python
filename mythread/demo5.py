#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Topic: 线程模块threading

"""

import time, threading


# 新线程执行的代码:
def loop():
    # threading模块有个current_thread()函数，它永远返回当前线程的实例
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
