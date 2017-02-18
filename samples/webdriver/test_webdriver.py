#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic:
1. 登录多说后台，将评论数据导出来，导出文件为comments.json
2. 通过selenium框架来模拟浏览器来登录多说后台，把所有评论的thread_id和文章标题拿出来，并删除所有评论
3. 去自己的博客http://yidao620c.github.io/网站去给每篇文章回复一下
4. 再次去多说后台，把所有评论的新的thread_id和文章标题拿出来
5. 然后将comments.json中旧的thread_id换成新的
6. 去多说后台把那个文章thread_key找出来，因为多说只认这个，然后更新每个post中的thread_key完成评论迁移


环境配置
selenium
pip install -U selenium

PhantomJS
这个不同的操作系统有各自对应的版本，官网下载页面 <http://phantomjs.org/download.html>
去下载你对应操作系统版本的phantomjs.下载完后，解压缩可以看到在文件夹的bin目录下有对应的phantomjs的可执行文件，
拷贝一份放入一个环境变量可以搜索到的地方，或者直接把phantomjs的bin目录加入环境变量即可~
"""
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


def fetch_map():
    driver = webdriver.Firefox()
    # 第一步，登录多说后台
    # browser.cookies.add({'duoshuo_unique': '4532c9aba164352d'})
    driver.get('http://duoshuo.com/')
    driver.find_element_by_xpath('//a[text()="登录"]').click()
    driver.find_element_by_xpath('//a[contains(text(), "QQ")]').click()
    # 进入iframe
    driver.switch_to.frame('ptlogin_iframe')
    driver.find_element_by_id('switcher_plogin').click()
    driver.find_element_by_id('u').send_keys('344063306')
    driver.find_element_by_id('p').send_keys('******')
    driver.find_element_by_id('login_button').click()
    # driver.switch_to.frame('vcode')
    # driver.find_element_by_id('capRefreshTips').click()
    # WebDriverWait(driver, 3).until(
    #     EC.presence_of_element_located((By.ID, "CAPTCHA_img"))
    # )
    # print(driver.find_element_by_id('CAPTCHA_img').get_attribute('url'))
    # driver.save_screenshot(r"D:\work\projects\core-python\temp\aa.png")
    # yanzm = input('验证码=')
    # driver.find_element_by_id('capAns').send_keys(yanzm)
    # driver.find_element_by_id('submit').click()
    # 返回主窗体
    # driver.switch_to.default_content()
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//a[contains(text(),"后台管理")]'))
    )
    driver.find_element_by_xpath('//a[contains(text(),"后台管理")]').click()
    driver.find_element_by_xpath('//a[contains(text(),"笨跑的一刀")]').click()
    link_map = dict()
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"笨跑的一刀的所有评论")]'))
    )
    while True:
        print('当前处理页面为第{}页'.format(
            driver.find_element_by_xpath('//span[@class="current-page-number"]').text))
        for ele in driver.find_elements_by_xpath(
                '//div/a[@class="pushstate-link" and not(@rel)]'):
            link_map[ele.text.strip()] = ele.get_attribute('data-thread-id')
        try:
            driver.find_element_by_xpath(
                '//div/a[@rel="next" and not(contains(@class, "disabled"))]').click()
            time.sleep(2)
        except NoSuchElementException:
            break
    print('全部页面处理完成！')
    driver.quit()
    for k, v in link_map.items():
        print("'{}': '{}'".format(k, v))
    return link_map


def replace_json(old_map, new_map):
    json_file = r'D:\work\projects\core-python\temp\export.json'
    result_map = dict()
    for k, v in old_map.items():
        result_map[v] = new_map[k]
    for k, v in result_map.items():
        print("'{}': '{}'".format(k, v))
    with open(json_file, mode='r', encoding='utf-8') as readf:
        lines = readf.readlines()
    last_lines = []
    for line in lines:
        for k, v in result_map.items():
            line = line.replace(k, v)
        last_lines.append(line)
    with open(json_file, mode='w', encoding='utf-8') as writef:
        writef.writelines(last_lines)


def replace_threadkey():
    map1 = {
        'Nginx的安装和配置': '6219151218892079874'
    }
    map2 = {
        'Nginx的安装和配置': '6260364880264561409'
    }
    map3 = {
        'Nginx的安装和配置': '2015/10/20/2015-10-20-nginx/'
    }
    mapmm = dict()
    for k, v in map2.items():
        mapmm[v] = map3[k]
    for k, v in mapmm.items():
        print("'{}': '{}'".format(k, v))
    json_file = r'D:\work\projects\core-python\temp\export.json'
    with open(json_file, mode='r', encoding='utf-8') as readf:
        lines = readf.readlines()
    for i in range(0, len(lines)):
        if '"thread_id"' in lines[i]:
            thread_id = lines[i].split(":")[1].strip()[:-1]
            continue
        if '"thread_key"' in lines[i]:
            if thread_id in mapmm:
                lines[i] = lines[i].replace('null', '"{}"'.format(mapmm[thread_id]))
    print('开始写文件')
    with open(json_file, mode='w', encoding='utf-8') as writef:
        writef.writelines(lines)


def click_page():
    driver = webdriver.Firefox()
    driver.get('http://yidao620c.github.io/archives/')
    driver.maximize_window()
    len1 = len(driver.find_elements_by_xpath(
                '//div[@class="post-archive"]/ul[@class="listing"]/li/a'))
    _log.info('开始自动点击页面...')
    for k in range(1, 100):
        logging.info('第{}轮开始...'.format(k))
        for i in range(0, len1):
            l_xpath = '(//div[@class="post-archive"]/ul[@class="listing"]/li/a)[{}]'.format(i + 1)
            ele = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.XPATH, l_xpath))
            )
            ele.click()
            driver.back()

    _log.info('all finished.')
    driver.close()

if __name__ == '__main__':
    pass
