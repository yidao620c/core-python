# -*- encoding: utf-8 -*-
"""
并发和并行

并发指的是同时具有多个活动的系统，多个任务需要同时进行，只需要单CPU就行。
并行则是同一个时刻有多个任务执行，需要多CPU。
"""

import asyncio
import time

now = lambda: time.time()


async def do_some_work(x):
    print("Waiting:", x)
    await asyncio.sleep(x)
    return "Done after {}s".format(x)


start = now()

coroutine1 = do_some_work(1)
coroutine2 = do_some_work(2)
coroutine3 = do_some_work(4)

tasks = [
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine3)
]

loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
loop.run_until_complete(asyncio.gather(*tasks))

for task in tasks:
    print("Task ret:", task.result())

print("Time:", now() - start)
