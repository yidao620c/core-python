#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Topic: multiprocessing创建进程
Desc : 
"""

# from multiprocessing import Process
# import os
#
#
# # 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Process will start.')
#     p.start()
#     # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
#     p.join()
#     print('Process end.')
#
# # Multiprocessing with Pipe
# # 这里的Pipe是双向的。
# # Pipe对象建立的时候，返回一个含有两个元素的表，每个元素代表Pipe的一端(Connection对象)。
# # 我们对Pipe的某一端调用send()方法来传送对象，在另一端使用recv()来接收。
# import multiprocessing as mul
#
# def proc1(pipe):
#     pipe.send('hello')
#     print('proc1 rec:', pipe.recv())
#
#
# def proc2(pipe):
#     print('proc2 rec:', pipe.recv())
#     pipe.send('hello, too')
#
# # Build a pipe
# pipe = mul.Pipe()
# # Pass an end of the pipe to process 1
# p1 = mul.Process(target=proc1, args=(pipe[0],))
# # Pass the other end of the pipe to process 2
# p2 = mul.Process(target=proc2, args=(pipe[1],))
# p1.start()
# p2.start()
# p1.join()
# p2.join()


# 下面演示怎样通过PIPE来获取multiprocessing.Process进程返回值
import multiprocessing

def worker(procnum, send_end):
    '''worker function'''
    result = str(procnum) + ' represent!'
    print(result)
    send_end.send(result)

def main():
    jobs = []
    pipe_list = []
    for i in range(5):
        # 单向管道返回的是(接受端，发送端)
        recv_end , send_end = multiprocessing.Pipe(False)
        p = multiprocessing.Process(target=worker, args=(i, send_end))
        jobs.append(p)
        pipe_list.append(recv_end)
        p.start()

    for proc in jobs:
        proc.join()
    result_list = [x.recv() for x in pipe_list]
    print(result_list)
    for x in pipe_list:
        x.close()

if __name__ == '__main__':
    main()

