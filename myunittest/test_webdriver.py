#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic:
1. 登录多说后台，将评论数据导出来，导出文件为comments.json
2. 通过HtmlUnit模拟浏览器来登录多说后台，然后把所有评论的thread_id和文章标题拿出来，并删除所有评论
3. 之后，我去自己的博客http://yidao620c.github.io/网站去给每篇文章回复一下
4. 再次去多说后台，把所有评论的新的thread_id和文章标题拿出来
5. 然后将comments.json中旧的thread_id换成新的，完成完整的评论迁移
"""
from selenium import webdriver


if __name__ == '__main__':
    # 测试下RemoteDriver，HtmlUnitDriver with enabled js
    driver = webdriver.Remote("http://localhost:4444/wd/hub",
                              webdriver.DesiredCapabilities.HTMLUNITWITHJS)
    driver.get('http://www.baidu.com/')
    id = driver.session_id
    driver.quit()
    pass
