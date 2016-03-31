#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
OSC对eechen的机器人回复
"""
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import random


def auto_comment():
    random.randint(0, 54)
    driver = webdriver.PhantomJS()
    # 第一步，登录多说后台
    # browser.cookies.add({'duoshuo_unique': '4532c9aba164352d'})
    driver.get('http://www.oschina.net/')
    driver.maximize_window()
    driver.find_element_by_xpath('//div[@id="OSC_Userbar"]/a[text()="登录"]').click()
    driver.find_element_by_id('f_email').send_keys("yidao620@gmail.com")
    driver.find_element_by_id('f_pwd').send_keys("baobao620")
    driver.find_element_by_xpath('//input[@value="现在登录 »"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//li[@id="hotSwitcher"]/a').click()
    driver.find_element_by_xpath('//a[@href="http://my.oschina.net/eechen/tweet/8355398"]').click()
    driver.find_element_by_id('edt_tweet_post_8355398').send_keys("爆菊测试开始[2][2][2]")
    driver.find_element_by_id('btn_submit').click()
    for i in range(1, 1000):
        print("开始随机回复%s" % (i,))
        time.sleep(1)
        r1 = random.randint(0, 54)
        r2 = random.randint(0, 54)
        r3 = random.randint(0, 54)
        driver.find_element_by_id('edt_tweet_post_8355398').send_keys(
            "@eechen python灌水机器人[%s][%s][%s]" % (r1, r2, r3))
        driver.find_element_by_id('btn_submit').click()


if __name__ == '__main__':
    auto_comment()
