# -*- encoding: utf-8 -*-
"""使用asyncio实现光标旋转动画
也就是文本式旋转指针（由 ASCII 字符 "|/-\" 构成的动画旋转指）
"""
import asyncio
import itertools
import sys


async def spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            await asyncio.sleep(.1)
        except asyncio.CancelledError:
            break


async def slow_function():
    # 假装等待I/O一段时间
    await asyncio.sleep(3)
    return 42


async def supervisor():
    spinner_task = spin('thinking!')
    slow_function_task = slow_function()
    tasks = [
        asyncio.ensure_future(spinner_task),
        asyncio.ensure_future(slow_function_task)
    ]
    results = await asyncio.gather(*tasks)
    # 等待完后把spinner这个Task取消掉
    tasks[0].cancel()
    return results[1]


def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(supervisor())
    print('Answer:', result)


if __name__ == '__main__':
    main()
