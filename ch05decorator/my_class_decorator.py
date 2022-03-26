# -*- encoding: utf-8 -*-
"""
类装饰器
类装饰器主要依赖于函数__call__()，每当你调用一个类的示例时，函数__call__()就会被执行一次。
"""


class Count:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print('num of calls is: {}'.format(self.num_calls))
        return self.func(*args, **kwargs)


@Count
def example():
    print("hello world")


example()
example()
