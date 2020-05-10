# -*- encoding: utf-8 -*-
"""
创建一个Task（Future类的子类）
"""

import asyncio
import time


async def do_some_work(x):
    print("waiting:", x)


start = time.time()
# 这里是一个协程对象，这个时候do_some_work函数并没有执行
coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = loop.create_task(coroutine)
print(task)
loop.run_until_complete(task)
print(task)
print("Time:", time.time() - start)
