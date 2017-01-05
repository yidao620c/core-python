#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
io demo
"""
__author__ = "Xiong Neng"

from io import StringIO, BytesIO
import os
import shutil
import pickle

def basic_rw():
    with open('/path/to/file', 'r', encoding='utf-8', errors='ignore') as f:
        print(f.read(200))  # 一次读取200字节bytes
        print(f.read())
    with open('/Users/michael/test.txt', 'w', encoding='utf-8') as f:
        f.write('Hello, world!')


def stringio_rw():
    f = StringIO()
    f.write('hello')
    f.write(' ')
    f.write('中文!')
    print(f.getvalue())

    f = StringIO('Hello!\nHi!\n中文!')
    while True:
        s = f.readline()
        if not s:
            break
        print(s.strip())


def bytesio_rw():
    f = BytesIO()
    f.write('中文'.encode('utf-8'))
    print(f.getvalue())


def file_dir():
    # 查看当前目录的绝对路径
    print(os.path.abspath('.'))
    # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
    os.path.join('/Users/michael', 'testdir')
    # 然后创建一个目录
    os.mkdir('/Users/michael/testdir')
    # 删掉一个目录:
    os.rmdir('/Users/michael/testdir')
    # 分开路径和文件名
    os.path.split('/Users/michael/testdir/file.txt')
    # 得到文件扩展名
    os.path.splitext('/path/to/file.txt')
    # 重命名
    os.rename('test.txt', 'test.py')
    # 删除文件
    os.remove('test.py')
    # 列出当前目录所有文件夹
    all_dir = [x for x in os.listdir('.') if os.path.isdir(x)]
    # 列出所有py文件
    all_py = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']


def _pickle():
    d = dict(name='Bob', age=20, score=88)
    # 序列化必须是二进制写入，不能文本形式
    with open('d:/dump.txt', 'wb') as f:
        pickle.dump(d, f)
    # 反序列化必须是二进制读取
    with open('d:/dump.txt', 'rb') as f:
        d = pickle.load(f)
        print(d)


def _json():
    """如果在不同语言直接传递对象，标准格式推荐是JSON
    JSON不仅是标准格式，并且比XML更快，
    而且可以直接在Web页面中读取，非常方便。
    """
    import json
    d = dict(name='Bob', age=20, score=88)
    json.dumps(d)  # 返回json字符串
    with open('d:/dump.txt', 'w', encoding='utf-8') as f:
        json.dump(d, f)
    json_str = '{"age": 20, "score": 88, "name": "Bob"}'
    dd = json.loads(json_str)
    print(dd)
    with open('d:/dump.txt', 'r', encoding='utf-8') as f:
        ddd = json.load(f)
        print(ddd)

    # 对象json序列化
    s = Student('Bob', 20, 88)
    # 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量
    j_str = json.dumps(s, default=lambda obj: obj.__dict__)
    print(j_str)
    # 对象json反序列化
    print(json.loads(j_str, object_hook=dict2student))
    # --------------------------------------------------
    # 更高级和复杂的对象json序列化使用第三方模块jsonpickle
    # 主页：http://jsonpickle.github.io/
    # ---------------------------------------------------


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

if __name__ == '__main__':
    stringio_rw()
    bytesio_rw()
    _pickle()
    _json()