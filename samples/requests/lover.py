#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 每天一句情话
"""
import requests
import re
from io import StringIO
import json
import xml.etree.ElementTree as ET
import random


def extract_content(xml):
    """xpath解析，或者使用lxml库"""
    doc = ET.fromstring(xml)
    tt= doc.findall("//div[@class='articleText']")
    print(tt)


def lover_sentences():
    """获取情话网的情话列表！"""
    url = 'http://www.siandian.com/qinghua/'
    # 读取返回结果
    r = requests.get(url)
    # 改变r.encoding
    encoding = re.search('content="text/html;\s*charset=(.*?)"', r.text).group(1)
    r.encoding = encoding

    finds = re.finditer(r'<a href="(.*?\.html)" class="articleTitle.*?>.*?</a>', r.text)
    for f in finds:
        find_cute("http://www.siandian.com{}".format(f.group(1)))
        break

def find_cute(url):
    # 读取返回结果
    r = requests.get(url)
    # 改变r.encoding
    encoding = re.search('content="text/html;\s*charset=(.*?)"', r.text).group(1)
    r.encoding = encoding
    # print(r.text)
    finds = re.finditer(r'<p>\s*([^>]*?)\s*\n', r.text)
    i = random.randint(0, sum(1 for _ in finds))
    start = 0
    finds = re.finditer(r'<p>\s*([^>]*?)\s*\n', r.text)
    for f in finds:
        if start == i:
            print(f.group(1))
            break
        start += 1


def main():
    lover_sentences()
