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
"""
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


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
    driver.find_element_by_id('p').send_keys('vs_baobao620817')
    driver.find_element_by_id('login_button').click()
    driver.switch_to.frame('vcode')
    # driver.find_element_by_id('capRefreshTips').click()
    # WebDriverWait(driver, 3).until(
    #     EC.presence_of_element_located((By.ID, "CAPTCHA_img"))
    # )
    # print(driver.find_element_by_id('CAPTCHA_img').get_attribute('url'))
    # driver.save_screenshot(r"D:\work\projects\core-python\temp\aa.png")
    yanzm = input('验证码=')
    driver.find_element_by_id('capAns').send_keys(yanzm)
    driver.find_element_by_id('submit').click()
    # 返回主窗体
    driver.switch_to.default_content()
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


if __name__ == '__main__':
    allkeys = {
        "2015/05/01/python-decorator.html",
        "2016/03/06/hexo.html",
        "2015/04/23/lvs-keepalived.html",
        "2015/04/23/pyinstaller.html",
        "2015/04/22/fastjson-date.html",
        "2015/04/21/simpleblog-14.html",
        "2015/04/21/simpleblog-13.html",
        "2015/04/21/simpleblog-12.html",
        "2015/04/21/simpleblog-11.html",
        "2015/04/21/simpleblog-10.html",
        "2015/04/21/simpleblog-08.html",
        "2015/04/21/simpleblog-07.html",
        "2015/04/21/simpleblog-06.html",
        "2015/04/21/simpleblog-05.html",
        "2015/04/20/simpleblog-04.html",
        "2015/04/20/simpleblog-03.html",
        "2015/04/20/simpleblog-02.html",
        "2015/04/21/simpleblog-09.html",
        "2015/04/20/simpleblog-01.html",
        "2016/03/08/scrapy-1.html",
        "2015/10/13/httpd-tomcat.html",
        "2015/10/10/centos-python.html",
        "guestbook/index.html",
        "2015/04/16/memcached-install.html",
        "2015/10/20/nginx.html",
        "2015/03/18/octopress-blog.html",
        "2015/03/07/joke.html",
        "about/index.html"
    }
    json_file = r'D:\work\projects\core-python\temp\export01.json'
    with open(json_file, mode='r', encoding='utf-8') as readf:
        lines = readf.readlines()
    pat = re.compile('.+"(.+)",')
    for i in range(0, len(lines)):
        if '"thread_key"' in lines[i]:
            s = pat.search(lines[i])
            if not s:
                print('not found:' + lines[i])
            else:
                thread_key = pat.search(lines[i]).group(1)
                if thread_key not in allkeys:
                    print(thread_key)
    # print('开始写文件')
    # with open(json_file, mode='w', encoding='utf-8') as writef:
    #     writef.writelines(lines)

    # s = '"thread_key": "2015/04/20/2015-04-20-simpleblog-04/",'
    # ss = re.sub('\d{4}-\d{2}-\d{2}-(.+)/', '\g<1>.html', s)
    # print(ss)
