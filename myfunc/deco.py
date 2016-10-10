# encoding: utf-8
"""
    Topic: sample
    Desc : 利用闭包演示带参的装饰器
"""
from time import time
from functools import wraps

__author__ = 'Xiong Neng'


def logged(when):
    def log(f, *args, **kargs):
        print('Called: function: %s, args: %r, kargs: %r' % (f, args, kargs))

    def pre_decorator(func):
        @wraps(func)
        def func_wrapper(*args, **kargs):
            log(func, *args, **kargs)
            return func(*args, **kargs)
        return func_wrapper

    def post_decorator(func):
        @wraps(func)
        def func_wrapper(*args, **kwargs):
            now = time()
            try:
                return func(*args, **kwargs)
            finally:
                log(func, *args, **kwargs)
                print('time delta: %s' % (time() - now))
        return func_wrapper

    try:
        return {'pre': pre_decorator, 'post': post_decorator}[when]
    except KeyError as e:
        raise ValueError(e, 'must be "pre" or "post"')


@logged('post')
def hello(name):
    print('Hello', name)


def tags(tag_name):
    def tags_decorator(func):
        @wraps(func)
        def func_wrapper(*args, **kargs):
            return "<{0}>{1}</{0}>".format(tag_name, func(*args, **kargs))
        return func_wrapper
    return tags_decorator


def pptags(func):
    @wraps(func)
    def func_wrapper(*args, **kargs):
        return "<{0}>{1}</{0}>".format('pp', func(*args, **kargs))
    return func_wrapper


@tags('p')
def get_text(name):
    """returns some text with p"""
    return "Hello " + name

@pptags
def get_text_pp(name):
    """returns some text with pp"""
    return "Hello " + name


if __name__ == '__main__':
    print(get_text.__name__)  # get_text
    print(get_text.__doc__)  # returns some text
    print(get_text.__module__)  # __main__
    print(get_text('韩梅梅'))

    print(get_text_pp.__name__)  # get_text
    print(get_text_pp.__doc__)  # returns some text
    print(get_text_pp.__module__)  # __main__
    print(get_text_pp('李雷'))
