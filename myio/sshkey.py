#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
desc: ssh-copy-id to other servers
更简单的方式使用：pip install pexpect

ssh-keygen和ssh-copy-id这些命令都直接作用于terminal
也就是你的tty设备，不会感知stdin，所以这里就不能使用Popen的stdin=PIPE来输入指令

:copyright: (c) 2017 by Xiong Neng.
:license: MIT, see LICENSE for more details.
"""
import shlex
from threading import Thread
from queue import Queue, Empty
import sys
import getpass
from subprocess import Popen, PIPE
import time
import os
try:
    from subprocess import DEVNULL  # Python 3.
except ImportError:
    DEVNULL = open(os.devnull, 'wb')

def main():
    if len(sys.argv) <= 1:
        print('you must specify the server ip')
        exit(1)
    server_ip = sys.argv[1]

    # pswd = getpass.getpass('Password: ')

    # p = Popen(shlex.split('ls ~/.ssh/id_rsa.pub'), stdout=PIPE, stderr=PIPE)
    # p.communicate()

    if not os.path.exists('/root/.ssh/id_rsa.pub'):
        p1 = Popen(shlex.split('ssh-keygen -t rsa -P "" -f /root/.ssh/id_rsa'), stdout=DEVNULL, stderr=DEVNULL)
        p1.wait()
        # p1.stdin.write('\n')
        # p1.stdin.write('\n')
        # p1.stdin.write('\n')
        # p1.stdin.close()
        # # wrap p.stdout with a NonBlockingStreamReader object:
        # nb_stdout = NonBlockingStreamReader(p1.stdout)
        # # issue command:
        # p1.stdin.write('\n')
        # # get the output
        # while True:
        #     output = nb_stdout.readline(0.2)  # 0.2 secs to let the shell output the result
        #     if not output:
        #         break
        #     print(output)
    ssh_cmd = 'ssh {} -o PasswordAuthentication=no StrictHostKeyChecking=no exit'.format(server_ip)
    p2 = Popen(shlex.split(ssh_cmd), stdout=DEVNULL, stderr=DEVNULL)
    p2.wait()
    if p2.returncode != 0:
        ssh_copy_id = 'ssh-copy-id -o StrictHostKeyChecking=no root@{}'.format(server_ip)
        p3 = Popen(shlex.split(ssh_copy_id), stdout=DEVNULL, stderr=DEVNULL)
        stdout, stderr = p3.communicate()
        if p3.returncode == 0:
            print('copy ssh key success!')
    else:
        print('do nothing!')


class NonBlockingStreamReader:
    def __init__(self, stream):
        """
        stream: the stream to read from.
                Usually a process' stdout or stderr.
        """
        self._s = stream
        self._q = Queue()

        def _populateQueue(stream, queue):
            """
            Collect lines from 'stream' and put them in 'quque'.
            """
            while True:
                line = stream.readline()
                if line:
                    queue.put(line)
                else:
                    raise UnexpectedEndOfStream

        self._t = Thread(target=_populateQueue, args=(self._s, self._q))
        self._t.daemon = True
        self._t.start()  # start collecting lines from the stream

    def readline(self, timeout=None):
        try:
            return self._q.get(block=timeout is not None, timeout=timeout)
        except Empty:
            return None


class UnexpectedEndOfStream(Exception): pass


if __name__ == '__main__':
    main()
