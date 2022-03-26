#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
停止协程，发送异常
"""


class DemoException(Exception):
    """为这次演示定义的异常类型。"""


def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoException handled. Continuing...')
        else:
            print('-> coroutine received: {!r}'.format(x))
    raise RuntimeError('This line should never run.')
