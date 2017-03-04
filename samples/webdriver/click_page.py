#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic:
去自己的博客网站去给每篇文章回复一下
"""
import gevent
from gevent.pool import Group, Pool
from gevent import monkey

monkey.patch_all()

import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import sys
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.StreamHandler(sys.stdout)])
# 模块基本用_，类级别用__
_log = logging.getLogger('app.' + __name__)
THREAD_COUNT = 30

def gevent_click_page():
    global TRY_COUNT
    TRY_COUNT = int(sys.argv[1])

    _log.info('自动点击页面开始...')
    # 先获取文章总篇数
    driver = webdriver.PhantomJS()
    driver.get('https://www.xncoding.com/archives/')
    # driver.maximize_window()
    posts_count = len(driver.find_elements_by_xpath(
        '//article/header/h1[@class="post-title"]/a[@class="post-title-link"]'))
    driver.close()
    # gevent的pool容量
    psize = posts_count / THREAD_COUNT
    _log.info('总的文章数量为:{}, 每组需要爬取的文章数:{}'.format(posts_count, psize))
    group = Group()
    for i in range(0, THREAD_COUNT + 1):
        group.add(gevent.spawn(_click_page, posts_count, psize, i))
    group.join()

    _log.info('成功结束...')

def _click_page(total_posts, pool_size, group_index):
    _log.info('第{}组: starting...'.format(group_index + 1))
    if group_index > 0 and total_posts < pool_size * group_index:
        return
    # 先获取文章总篇数
    _driver = webdriver.PhantomJS()
    _driver.get('https://www.xncoding.com/archives/')

    global TRY_COUNT
    for k in range(1, TRY_COUNT + 1):
        # _log.info('第{}组: 第{}轮开始...'.format(group_index + 1, k))
        for i in range(pool_size * group_index, min(pool_size * (group_index + 1), total_posts)):
            l_xpath = '(//article/header/h1[@class="post-title"]/a[@class="post-title-link"])[{}]'.format(i + 1)
            ele = WebDriverWait(_driver, 2).until(
                EC.presence_of_element_located((By.XPATH, l_xpath))
            )
            ele.click()
            WebDriverWait(_driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="post-body"]'))
            )
            _driver.back()

    _log.info('第{}组: finished.'.format(group_index + 1))
    _driver.close()


def just_click():
    # 先获取文章总篇数
    _driver = webdriver.PhantomJS()
    _driver.get('https://www.xncoding.com/archives/')
    # driver.maximize_window()
    posts_count = len(_driver.find_elements_by_xpath(
        '//article/header/h1[@class="post-title"]/a[@class="post-title-link"]'))
    for cc in range(1, posts_count + 1):
        l_xpath = '(//article/header/h1[@class="post-title"]/a[@class="post-title-link"])[{}]'.format(cc)
        ele = WebDriverWait(_driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, l_xpath))
        )
        _log.info('点击第{}篇文章'.format(cc))
        ele.click()
        WebDriverWait(_driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="post-body"]'))
        )
        _driver.back()

if __name__ == '__main__':
    _log.info('自动点击页面开始...')
    just_click()
    _log.info('成功结束...')
