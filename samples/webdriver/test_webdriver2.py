#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic:
因为域名修改原因将源博客地址修正，那么多说评论跟着迁移
1. 通过selenium框架来模拟浏览器来登录多说后台
2. 进入文章设置页面，将所有文章链接前缀由“http://yidao620c.github.io/”修改成“https://www.xncoding.com/”

环境配置
selenium
pip install -U selenium

selenium 3.x开始，firefox 47以上版本，需要下载第三方driver，即geckodriver
https://github.com/mozilla/geckodriver/releases
下载到任意电脑任意目录，解压后将该路径加入到PC的path（针对windows）即可。简单点直接放C:\Windows目录下面

PhantomJS
这个不同的操作系统有各自对应的版本，官网下载页面 <http://phantomjs.org/download.html>
去下载你对应操作系统版本的phantomjs.下载完后，解压缩可以看到在文件夹的bin目录下有对应的phantomjs的可执行文件，
拷贝一份放入一个环境变量可以搜索到的地方，或者直接把phantomjs的bin目录加入环境变量即可~
"""
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
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
old_pre = 'http://yidao620c.github.io/'
new_pre = 'https://www.xncoding.com/'

def replace_linkpre():
    driver = webdriver.Firefox()
    driver.get('http://duoshuo.com/')
    driver.maximize_window()
    # 第一步，登录多说后台
    # browser.cookies.add({'duoshuo_unique': '4532c9aba164352d'})
    driver.find_element_by_xpath('//a[text()="登录"]').click()
    driver.find_element_by_xpath('//a[contains(text(), "QQ")]').click()
    # 进入iframe
    frame = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ptlogin_iframe")))
    driver.switch_to.frame(frame)
    # driver.switch_to_frame(driver.find_element_by_id('ptlogin_iframe'))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "switcher_plogin")))
    driver.find_element_by_id('switcher_plogin').click()
    u = driver.find_element_by_id('u')
    u.clear()
    u.send_keys('344063306')
    p = driver.find_element_by_id('p')
    p.clear()
    p.send_keys('********')
    driver.find_element_by_id('login_button').click()
    # 返回主窗体
    driver.switch_to.default_content()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"后台管理")]'))
    )
    driver.find_element_by_xpath('//a[contains(text(),"后台管理")]').click()
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"笨跑的一刀")]')))
    driver.find_element_by_xpath('//a[contains(text(),"笨跑的一刀")]').click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'icon-thread')))
    # driver.find_element_by_xpath('//a/span[@id="icon-thread"]/parent::a').click()
    driver.find_element_by_xpath('//li[@class="tab-thread"]').click()
    current_num = 1
    while True:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//span[@class="current-page-number"]'))
        )
        current_num = int(driver.find_element_by_xpath('//span[@class="current-page-number"]').text)
        print('当前处理页面为第{}页'.format(current_num))
        for tr in driver.find_elements_by_xpath('//table[contains(@class, "thread-table")]/tbody/tr'):
            old_link = tr.find_element_by_xpath('./td[@class="thread-title"]/a[1]').get_attribute('href')
            print(old_link)
            tr.find_element_by_xpath('./td/a[@class="edit-thread" and text()="编辑"]').click()
            oinput = '//div[@style="display: block;"]//form//label[text()="文章网址"]/' \
                     'following-sibling::div/input[@value="{}"]'.format(old_link)
            print(oinput)
            WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, oinput))
            )
            if old_link.startswith(old_pre):
                new_link = old_link.replace(old_pre, new_pre)
                driver.find_element_by_xpath(oinput).clear()
                driver.find_element_by_xpath(oinput).send_keys(new_link)
                driver.find_element_by_xpath(
                    '//div[@style="display: block;"]//form//button[text()="保存"]').click()
            else:
                driver.find_element_by_xpath(
                    '//div[@style="display: block;"]//form//button[text()="取消"]').click()
        try:
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//div/a[@rel="next" and not(contains(@class, "disabled"))]'))
            )
            driver.find_element_by_xpath(
                '//div/a[@rel="next" and not(contains(@class, "disabled"))]').click()
            current_num += 1
            current_num_xpath = '//span[@class="current-page-number" and text()="{}"]'.format(current_num)
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, current_num_xpath))
            )
        except NoSuchElementException:
            break
    print('全部页面处理完成！')
    driver.quit()


def replace_linkpre1():
    """已经登录了QQ的情况"""
    profile = webdriver.FirefoxProfile()
    profile.set_preference("webdriver.load.strategy", "unstable")
    driver = webdriver.Firefox(firefox_profile=profile)
    driver.get('http://duoshuo.com/')
    driver.maximize_window()
    # 第一步，登录多说后台
    # browser.cookies.add({'duoshuo_unique': '4532c9aba164352d'})
    driver.find_element_by_xpath('//a[text()="登录"]').click()
    driver.find_element_by_xpath('//a[contains(text(), "QQ")]').click()
    # 进入iframe
    frame = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ptlogin_iframe")))
    driver.switch_to.frame(frame)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@uin="344063306"]')))
    driver.find_element_by_xpath('//a[@uin="344063306"]').click()
    # 返回主窗体
    driver.switch_to.default_content()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"后台管理")]'))
    )
    driver.find_element_by_xpath('//a[contains(text(),"后台管理")]').click()
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"笨跑的一刀")]')))
    driver.find_element_by_xpath('//a[contains(text(),"笨跑的一刀")]').click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'icon-thread')))
    # driver.find_element_by_xpath('//a/span[@id="icon-thread"]/parent::a').click()
    driver.find_element_by_xpath('//li[@class="tab-thread"]').click()
    link_set = set()
    while True:
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//span[@class="current-page-number"]'))
            )
            llen = len(driver.find_elements_by_xpath('//table[contains(@class, "thread-table")]/tbody/tr'))
        except StaleElementReferenceException:
            driver.refresh()
            driver.refresh()
            continue
        for i in range(1, llen + 1):
            row_xpath = '//table[contains(@class, "thread-table")]/tbody/tr[{}]'.format(i)
            link_x = '{}/td[@class="thread-title"]/a[1]'.format(row_xpath)
            try:
                WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.XPATH, link_x))
                )
            except TimeoutException as e:
                driver.refresh()
                driver.refresh()
                continue
            try:
                old_link = driver.find_element_by_xpath(link_x).get_attribute('href')
            except StaleElementReferenceException:
                driver.refresh()
                driver.refresh()
                continue
            if old_link in link_set:
                continue
            link_set.add(old_link)
            if old_link.startswith(old_pre):
                edit_x = '{}/td/a[@class="edit-thread" and text()="编辑"]'.format(row_xpath)
                edit_ele = driver.find_element_by_xpath(edit_x)
                print(old_link)
                try:
                    driver.execute_script("return arguments[0].scrollIntoView(true);", edit_ele)
                    driver.find_element_by_xpath(edit_x).click()
                    oinput = '//div[@style="display: block;"]//form//label[text()="文章网址"]/' \
                             'following-sibling::div/input[@value="{}"]'.format(old_link)
                    WebDriverWait(driver, 3).until(
                        EC.presence_of_element_located((By.XPATH, oinput))
                    )
                except StaleElementReferenceException:
                    driver.refresh()
                    continue
                new_link = old_link.replace(old_pre, new_pre)
                driver.find_element_by_xpath(oinput).clear()
                driver.find_element_by_xpath(oinput).send_keys(new_link)
                driver.find_element_by_xpath(
                    '//div[@style="display: block;"]//form//button[text()="保存"]').click()
                # driver.get('http://yidao620c.duoshuo.com/admin/thread/')
                driver.refresh()
                driver.refresh()
        try:
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//div/a[@rel="next" and not(contains(@class, "disabled"))]'))
            )
            driver.find_element_by_xpath(
                '//div/a[@rel="next" and not(contains(@class, "disabled"))]').click()
            time.sleep(2)
            driver.implicitly_wait(3)
            current_num = int(driver.find_element_by_xpath('//span[@class="current-page-number"]').text)
            print('当前处理页面为第{}页'.format(current_num))
            current_num_xpath = '//span[@class="current-page-number" and text()="{}"]'.format(current_num)
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, current_num_xpath))
            )
        except (NoSuchElementException, TimeoutException) as e:
            break
    print('全部页面处理完成！')
    driver.quit()


if __name__ == '__main__':
    replace_linkpre1()
