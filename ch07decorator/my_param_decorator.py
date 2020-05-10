#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 参数化装饰器
"""

registry = set()


def register(active=True):
    """这时候register函数不是装饰器，而是装饰器工厂函数"""

    def decorate(func):
        """decorate这个内部函数是真正的装饰器"""
        print('running register(active=%s)->decorate(%s)' % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func

    return decorate


@register(active=False)  # @register工厂函数必须作为函数调用
def f1():
    print('running f1()')
