#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 装饰器示例
Desc : 
"""


def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

def strong_decorate(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))
    return func_wrapper

def div_decorate(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))
    return func_wrapper

@div_decorate
@p_decorate
@strong_decorate
def get_text(name):
   return "hello, {0}".format(name)

print(get_text("zhangsan"))



def p_decorate(func):
   def func_wrapper(*args, **kwargs):
       return "<p>{0}</p>".format(func(*args, **kwargs))
   return func_wrapper

class Person(object):
    def __init__(self):
        self.name = "Name"
        self.family = "Xiong"

    @p_decorate
    def get_fullname(self):
        return self.name+" "+self.family

my_person = Person()
print(my_person.get_fullname())


from functools import wraps

def tags(tag_name):
    def tags_decorator(func):
        @wraps(func)
        def func_wrapper(*args, **kargs):
            return "<{0}>{1}</{0}>".format(tag_name, func(*args, **kargs))
        return func_wrapper
    return tags_decorator

@tags("div")
@tags("p")
@tags("strong")
def get_text(name):
    return "hello, "+name

if __name__ == '__main__':
    print(get_text.__name__)  # get_text
    print(get_text.__doc__)  # returns some text
    print(get_text.__module__)  # __main__
    print(get_text('zhangsan'))

