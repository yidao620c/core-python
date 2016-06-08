#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 随机替换
Desc :
"""

import os
import sys
import re
import codecs
import random
reload(sys)
sys.setdefaultencoding('utf-8')

hanzi = [u'我', u'还', u'有', u'英', u'语', u'是', u'哈', u'好', u'多', u'星', u'早', u'测']
yingwen = ['coo', 'las', 'mus', 'bib', 'hah']
zimu = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q']


def randomID1():
    # 数字，4位数字以内
    return str(random.randint(1, 9999))


def randomID2():
    # 字母、数字10位长度以内
    random.shuffle(zimu)
    return u'{0}{1}'.format(''.join(zimu[:6]), random.randint(1000, 9999))


def randomName1():
    # 中文、字母、数字10位长度以内
    random.shuffle(hanzi)
    return u'{0}{1}{2}'.format(''.join(hanzi[:4]), random.choice(yingwen), random.randint(11, 99))


def randomName2():
    # 中文、字母、数字10位长度以内
    return randomName1()


def randomName3():
    # 字母、数字+.com 10位长度以内
    return randomName1()


def randomName4():
    # 中文、字母、数字10位长度以内
    random.shuffle(zimu)
    return u'{0}{1}.com'.format(''.join(zimu[:3]), random.randint(100, 999))


def randomName5():
    # 中文、字母、数字10位长度以内
    return randomName4()


def search_replace(fname):
    with codecs.open(fname, mode='r', encoding='utf-8') as readf:
        old_lines = readf.readlines()
    sep = os.linesep

    for i in range(0, len(old_lines)):
        # old_lines[i] = old_lines[i].rtrim()
        if u'"新增纳管系统"' in old_lines[i]:
            line5 = old_lines[i + 5]
            index5 = line5.find('"id":')
            old_lines[i + 5] = u'{0}{1}"{2}",{3}'.format(line5[:index5], '"id":', randomID1(), sep)

            line6 = old_lines[i + 6]
            index6 = line6.find('"name":')
            old_lines[i + 6] = u'{0}{1}"{2}",{3}'.format(line6[:index6], '"name":', randomName1(), sep)
        elif u'"新增本地组织"' in old_lines[i]:
            line5 = old_lines[i + 5]
            index5 = line5.find('"name":')
            old_lines[i + 5] = u'{0}{1}"{2}",{3}'.format(line5[:index5], '"name":', randomName2(), sep)
        elif u'"新增本地用户1"' in old_lines[i]:
            line5 = old_lines[i + 5]
            index5 = line5.find('"id":')
            old_lines[i + 5] = u'{0}{1}"{2}",{3}'.format(line5[:index5], '"id":', randomID2(), sep)
        elif u'"3.1.1.4.7新增角色"' in old_lines[i]:
            line5 = old_lines[i + 5]
            index5 = line5.find('"name":')
            old_lines[i + 5] = u'{0}{1}"{2}",{3}'.format(line5[:index5], '"name":', randomName3(), sep)
        elif u'"新增AD域配置"' in old_lines[i]:
            line5 = old_lines[i + 5]
            index5 = line5.find('"name":')
            old_lines[i + 5] = u'{0}{1}"{2}",{3}'.format(line5[:index5], '"name":', randomName4(), sep)
        elif u'"修改AD域配置"' in old_lines[i]:
            line5 = old_lines[i + 5]
            index5 = line5.find('"name":')
            old_lines[i + 5] = u'{0}{1}"{2}",{3}'.format(line5[:index5], '"name":', randomName5(), sep)
    with codecs.open(fname, mode='w', encoding='utf-8') as writef:
        writef.writelines(old_lines)


def search_replace2(file_path):
    from tempfile import mkstemp
    from shutil import move
    from os import remove, close
    replacements = {u'{randomID1}':randomID1(),
                    u'{randomName1}':randomName1(),
                    u'{randomName2}':randomName2(),
                    u'{randomID2}':randomID2(),
                    u'{randomName3}':randomName3(),
                    u'{randomName4}':randomName4(),
                    u'{randomName5}':randomName5()
                    }
    fh, abs_path = mkstemp()
    with open(abs_path,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                for k, v in replacements.items():
                    line = line.replace(k, v)
                new_file.write(str(line))
    close(fh)
    remove(file_path)
    move(abs_path, file_path)


if __name__ == '__main__':
    # sudo python replace_ip.py fname
    # search_replace(sys.argv[1])
    # thismodule = sys.modules[__name__]
    search_replace2('D:/download/20160524/z.txt')
    pass
