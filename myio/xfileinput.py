#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
fileinput模块演示

【基本格式】
fileinput.input([files[, inplace[, backup[, bufsize[, mode[, openhook]]]]]])
【默认格式】
fileinput.input (files=None, inplace=False, backup='', bufsize=0, mode='r', openhook=None)

【参数说明】
files:                  #文件的路径列表，默认是stdin方式，多文件['1.txt','2.txt',...]
inplace:                #是否将标准输出的结果写回文件，默认不取代
backup:                 #备份文件的扩展名，只指定扩展名，如.bak。如果该文件的备份文件已存在，则会自动覆盖。
bufsize:                #缓冲区大小，默认为0，如果文件很大，可以修改此参数，一般默认即可
mode:                   #读写模式，默认为只读
openhook:               #该钩子用于控制打开的所有文件，比如说编码方式等;

【常用函数】
fileinput.input()       #返回能够用于for循环遍历的对象
fileinput.filename()    #返回当前文件的名称
fileinput.lineno()      #返回当前已经读取的行的数量（或者序号）
fileinput.filelineno()  #返回当前读取的行的行号
fileinput.isfirstline() #检查当前行是否是文件的第一行
fileinput.isstdin()     #判断最后一行是否从stdin中读取
fileinput.close()       #关闭队列

:copyright: (c) 2017 by Xiong Neng.
:license: MIT, see LICENSE for more details.
"""
import sys
import glob
import fileinput


def t01():
    """利用fileinput读取一个文件所有行"""
    for line in fileinput.input('data.txt'):
        print(line.rstrip())

def t02():
    """读取文件名，行，内容"""
    for line in fileinput.input('data.txt'):
        print(fileinput.filename(), '|', 'Line Number:',
              fileinput.lineno(), '|: ', line)

def t03():
    """利用fileinput对多文件操作，并原地修改内容"""

    def process(line):
        return line.rstrip() + ' line'

    for line in fileinput.input(['1.txt', '2.txt'], inplace=1):
        print(process(line))

def t04():
    """利用fileinput实现文件内容替换，并将原文件作备份"""
    for line in fileinput.input('data.txt', backup='.bak', inplace=1):
        print(line.rstrip().replace('Python', 'Perl'))

def t05():
    """利用fileinput将CRLF文件转为LF"""
    for line in fileinput.input('data.txt', inplace=1):
        if line[-2:] == "\r\n":
            print(line.rstrip() + "\n")
        else:
            print(line.rstrip())

def t06():
    """利用fileinput批处理文件"""
    for line in fileinput.input(glob.glob("d*.txt"), inplace=1):
        if fileinput.isfirstline():
            print('-' * 20, 'Reading %s...' % fileinput.filename(), '-' * 20)
        print(str(fileinput.lineno()) + ': ' + line.rstrip().upper())

def t07():
    """利用fileinput及re做日志分析: 提取所有含日期的行"""
    import re
    pattern = '\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
    for line in fileinput.input('error.log', backup='.bak', inplace=1):
        if re.search(pattern, line):
            # 下面不自动添加换行
            sys.stdout.write("=> ")
            sys.stdout.write(line)
def t08():
    """利用fileinput实现类似于grep的功能"""
    import re
    pattern = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')
    for line in fileinput.input('data.txt', backup='.bak', inplace=1):
        if pattern.search(line):
            print(fileinput.filename(), fileinput.filelineno(), line)
def t09():
    """利用fileinput做正则替换"""
    import re
    pattern = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')
    for line in fileinput.input('data.txt', backup='.bak', inplace=1):
        line = re.sub(r'\* (.*)#(.*)', r'<h2 id="\2">\1</h2>', line.rstrip())
        print(line)


if __name__ == '__main__':
    t01()
    t02()
    t03()
    t04()
    t05()
    t06()
    t08()
    t09()
