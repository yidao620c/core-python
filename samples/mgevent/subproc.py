#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import shlex
import gevent
from gevent.subprocess import Popen, PIPE
from mycore.logmsg import get_log
_log = get_log(__name__)


def _split_list(lst, symbol):
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


def proc_cmd(cmd, **kwargs):
    """
    :param cmd:
    数组形式: ['ceph', 'osd', 'dump', '|', 'grep', 'poolname']
    字符串形式: 'ceph osd dump | grep "poolname"'
    kwargs传递其他额外参数，比如timeout=60，sudo=True等
    """
    sudo = kwargs.get('sudo', True)
    timeout = kwargs.get('timeout', 20)
    # 字符串命令转换成数组
    if isinstance(cmd, str):
        cmd = shlex.split(cmd)
    _log.info('proc_cmd command: {}'.format(cmd))
    # 为了处理好管道的情况，程序限定 '|' 分割写法
    all_cmd_list = list(_split_list(cmd, '|'))
    len_arg = len(all_cmd_list)
    if len_arg == 1:
        cmd_args = all_cmd_list[0]
        if sudo:
            cmd_args.insert(0, 'sudo')
        proc = Popen(cmd_args, close_fds=True, stdout=PIPE, stderr=PIPE)
        try:
            with gevent.Timeout(timeout, False):
                stdout, stderr = proc.communicate()
            if proc.returncode is None:
                _log.error("gevent.Timeout.cmd={},timeout={}".format(cmd, timeout))
                if proc:
                    kill_p = Popen(['sudo', 'kill', '--', str(proc.pid)], close_fds=True)
                    kill_p.wait()
                return 2, '', 'timeout error'
            return proc.returncode, stdout, stderr
        except Exception:
            if proc:
                # proc.kill()
                kill_p = Popen(['sudo', 'kill', '--', str(proc.pid)], close_fds=True)
                kill_p.wait()
            _log.error("proc_cmd unknownerror: cmd={}".format(cmd), exc_info=1)
            return 3, '', 'proc_cmd unknown error'
    else:
        if sudo:
            all_cmd_list[0].insert(0, 'sudo')
        p1 = Popen(all_cmd_list[0], stdout=PIPE)
        for cmd_middle in all_cmd_list[1:-1]:
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
                _log.error("gevent.Timeout.cmd={},timeout={}".format(cmd, timeout))
                return 2, '', 'timeout error'
        except Exception as e:
            if p2:
                # p2.kill()
                kill_p = Popen(['sudo', 'kill', '--', str(p2.pid)], close_fds=True)
                kill_p.wait()
            _log.error("proc_cmd unknownerror: cmd={}".format(cmd), exc_info=1)
            return 3, '', 'proc_cmd unknown error'
        return p2.returncode, stdout, stderr

