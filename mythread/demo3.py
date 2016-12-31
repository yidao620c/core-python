#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Topic: 进程池
Desc : 
"""

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    # Pool默认的大小时CUP核心数，这个是有意这样设计的
    p = Pool()
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    # 对Pool对象调用join()方法会等待所有子进程执行完毕，
    # 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
    p.close()
    p.join()
    print('All subprocesses done.')

