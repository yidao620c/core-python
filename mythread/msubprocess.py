#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    Topic: sample
    Desc : 
"""
import subprocess
__author__ = 'Xiong Neng'

def demo():
    # 执行基本系统命令
    ret = subprocess.call('ls -l', shell=True)
    # 静默执行基本系统命令
    ret = subprocess.call('rf -f *.java', shell=True,
                          stdout=open('/dev/null'))
    # 执行命令，但是捕捉输出
    p = subprocess.Popen('ls -l', shell=True,
                         stdout=subprocess.PIPE)
    out = p.stdout.read()
    # 执行命令，但是发送输入和接受输出
    p = subprocess.Popen('wc', shell=True, stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate('.')
    # 创建两个子进程，然后通过管道将它们连接在一起
    p1 = subprocess.Popen('ls -l', stdout=subprocess.PIPE)
    p2 = subprocess.Popen('wc', stdin=p1.stdout, stdout=subprocess.PIPE)
    p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
    stdout, stderr = p2.communicate()
    return p2.returncode, stdout, stderr

if __name__ == '__main__':
    a,b,c=1
    pass
