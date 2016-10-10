#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: unicode演示
Desc : 
"""


def person(name, age, height=11, *args, **kw):
    print('person() function...')
    pass


x = 'ABC'
print(x.encode('ascii'))
print(u''.encode('utf-8'))
print('\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))


my_string = "Hello World."


print(type(my_string))

my_unicode = u"Hi \u2119\u01b4\u2602\u210c\xf8\u1f24"
print(len(my_unicode))
print(my_unicode.encode('utf-8'))
print(len(my_unicode.encode('utf-8')))

my_unicode = u"Hi ℙƴ☂ℌøἤ"
print(len(my_unicode))



