# -*- encoding: utf-8 -*-
"""
协程嵌套

使用async可以定义协程，协程用于耗时的io操作，我们也可以封装更多的io操作过程，
这样就实现了嵌套的协程，即一个协程中await了另外一个协程，如此连接起来。
"""

import asyncio
import time

now = lambda: time.time()


async def do_some_work(x):
    print("waiting:", x)
    await asyncio.sleep(x)
    return "Done after {}s".format(x)


async def main():
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(4)
    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]
    return await asyncio.gather(*tasks)
    # # 这里使用await等待另一个或多个协程运行完
    # dones, pendings = await asyncio.wait(tasks)
    # for task in dones:
    #     print("Task ret:", task.result())

    # results = await asyncio.gather(*tasks)
    # for result in results:
    #     print("Task ret:",result)

    # for task in asyncio.as_completed(tasks):
    #     result = await task
    #     print("Task ret: {}".format(result))


start = now()

loop = asyncio.get_event_loop()
# 不在main协程函数里处理结果，直接返回await的内容，run_until_complete将会返回main协程的结果。
results = loop.run_until_complete(main())
for result in results:
    print("Task ret:", result)
print("Time:", now() - start)
