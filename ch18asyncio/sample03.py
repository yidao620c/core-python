# -*- encoding: utf-8 -*-
"""
绑定回调，在task执行完成的时候可以获取执行的结果，回调的最后一个参数是future对象，通过该对象可以获取协程返回值。
"""

import asyncio
import time

now = lambda: time.time()


async def do_some_work(x):
    print("waiting:", x)
    return "Done after {}s".format(x)


def callback(future):
    print("callback:", future.result())


start = now()
coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
print(task)
task.add_done_callback(callback)
print(task)
loop.run_until_complete(task)

print("Time:", now() - start)
