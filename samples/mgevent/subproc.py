#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import shlex
import gevent
from gevent.subprocess import Popen, PIPE
from functools import wraps
import os
import signal

def split_list(lst, symbol):
    item = []
    for i, e in enumerate(lst):
        if e == symbol:
            yield item
            item = []
        elif i == len(lst) - 1:
            item.append(str(e))
            yield item
        else:
            item.append(str(e))


def auto_log(log):
    def _auto_log(func):
        @wraps(func)
        def proc_cmd(cmd, *args, **kwargs):
            """
            timeout 默认设置为20s
            """
            origin_args = str(cmd) + " " + str(args)  # for error return
            sudo = kwargs.get('sudo', True)  ## 后面再考虑改成False
            timeout = kwargs.get('timeout', 20)

            if isinstance(cmd, list):  # 为了兼容以前的代码
                flatten_cmd_list = cmd + list(args)
            elif isinstance(cmd, str) and cmd:
                flatten_cmd_list = shlex.split(cmd) + list(args)
            else:
                flatten_cmd_list = [cmd] + list(args)
            # 为了处理好管道的情况，程序限定 '|' 分割写法
            all_cmd_list = list(split_list(flatten_cmd_list, '|'))

            len_arg = len(all_cmd_list)
            if (len_arg == 1):
                cmd_args = all_cmd_list[0]
                if sudo:
                    cmd_args.insert(0, 'sudo')
                proc = Popen(cmd_args, close_fds=True, stdout=PIPE, stderr=PIPE)
                try:
                    with gevent.Timeout(timeout, False):
                        stdout, stderr = proc.communicate()
                    if proc.returncode is None:
                        log.error("cmd={},timeout={}".format(flatten_cmd_list, timeout))
                        if proc:
                            # proc.kill()
                            kill_p = Popen(['sudo', 'kill', '--', str(proc.pid)], close_fds=True)
                            kill_p.wait()
                        return 2, '', 'timeout error'
                    return proc.returncode, stdout, stderr
                except Exception as e:
                    if proc:
                        # proc.kill()
                        kill_p = Popen(['sudo', 'kill', '--', str(proc.pid)], close_fds=True)
                        kill_p.wait()
                    log.error("cmd unknownerror: {0} error: {1}".format(origin_args, e))
                    return 3, '', 'unknown error'
            else:
                if sudo:
                    all_cmd_list[0].insert(0, 'sudo')
                p1 = Popen(all_cmd_list[0], stdout=PIPE)
                for cmd_middle in all_cmd_list[1:-1]:
                    print('cmd_middle={}'.format(cmd_middle))
                    if sudo:
                        cmd_middle.insert(0, 'sudo')
                    p2 = Popen(cmd_middle, stdin=p1.stdout, stdout=PIPE, stderr=PIPE)
                    p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
                    p1 = p2
                if sudo:
                    all_cmd_list[-1].insert(0, 'sudo')
                p2 = Popen(all_cmd_list[-1], stdin=p1.stdout, stdout=PIPE, stderr=PIPE)
                p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
                try:
                    with gevent.Timeout(timeout, False):
                        stdout, stderr = p2.communicate()
                    if p2.returncode is None:
                        if p2:
                            # p2.kill()
                            kill_p = Popen(['sudo', 'kill', '--', str(p2.pid)], close_fds=True)
                            kill_p.wait()
                        log.error("cmd={},timeout={}".format(flatten_cmd_list, timeout))
                        return 2, '', 'timeout error'
                except Exception as e:
                    if p2:
                        # p2.kill()
                        kill_p = Popen(['sudo', 'kill', '--', str(p2.pid)], close_fds=True)
                        kill_p.wait()
                    log.error("cmd unknownerror: {0} error: {1}".format(origin_args, e))
                    return 3, '', 'unknown error'
                return p2.returncode, stdout, stderr

        return proc_cmd

    return _auto_log
