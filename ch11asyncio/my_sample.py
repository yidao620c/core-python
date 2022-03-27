# -*- encoding: utf-8 -*-
"""
description
"""

import asyncio
import datetime

import asyncio


async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))


async def main(urls):
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    # for task in tasks:
    #     await task
    await asyncio.gather(*tasks)


########## 输出 ##########

print(datetime.datetime.now())
asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
print(datetime.datetime.now())
