# -*- encoding: utf-8 -*-
"""
description
"""

import asyncio
import functools


def print_log(func):
    """
    这里异步函数场景貌似不成功。
    :param func:
    :return:
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} start")
        res = func(*args, **kwargs)
        print(f"{func.__name__} end")
        return res

    return wrapper


async def worker_1():
    print('worker_1 start')
    await asyncio.sleep(1)
    print('worker_1 end')
    return 1


async def worker_2():
    print('worker_2 start')
    await asyncio.sleep(2)
    print('worker_2 end')
    return 2 / 0


async def worker_3():
    print('worker_3 start')
    await asyncio.sleep(3)
    print('worker_3 end')
    return 3


async def main():
    print('1111111111111111111111')
    task_1 = asyncio.create_task(worker_1())
    print('222222222222222222222')
    task_2 = asyncio.create_task(worker_2())
    print('33333333333333333333333')
    task_3 = asyncio.create_task(worker_3())
    print('444444444444444444444444')
    await asyncio.sleep(2)
    print('555555555555555555555555555')
    task_3.cancel()
    print('6666666666666666666666666666')
    res = await asyncio.gather(task_1, task_2, task_3, return_exceptions=True)
    print('77777777777777777777777777777')
    print(res)


asyncio.run(main())

########## 输出 ##########
