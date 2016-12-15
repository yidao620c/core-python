#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Topic: 线程池简单例子
Desc : 
"""


from multiprocessing.dummy import Pool as ThreadPool
import time,random

def hello(str):
    time.sleep(2)
    print(str)
    return str

def print_result(request, result):
    print("the result is %s %r" % (request.requestID, result))

data = [random.randint(1,10) for i in range(20)]
# Make the Pool of workers
pool = ThreadPool(20)
# Open the urls in their own threads
# and return the results
results = pool.map(hello, data)
#close the pool and wait for the work to finish
pool.close()
pool.join()

