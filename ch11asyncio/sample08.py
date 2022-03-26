# -*- encoding: utf-8 -*-
"""
不同线程的事件循环

很多时候，我们的事件循环用于注册协程，而有的协程需要动态的添加到事件循环中。一个简单的方式就是使用多线程。
当前线程创建一个事件循环，然后在新建一个线程，在新线程中启动事件循环。当前线程不会被block。
"""
import asyncio
import time
from threading import Thread

now = lambda: time.time()


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


def more_work(x):
    print('More work {}'.format(x))
    time.sleep(x)
    print('Finished more work {}'.format(x))


start = now()
new_loop = asyncio.new_event_loop()
t = Thread(target=start_loop, args=(new_loop,))
t.start()
print('TIME: {}'.format(time.time() - start))

# 顺序执行下面的回调函数
new_loop.call_soon_threadsafe(more_work, 3)
new_loop.call_soon_threadsafe(more_work, 6)

# 下面这条语句不会阻塞
print('===============last==============')
