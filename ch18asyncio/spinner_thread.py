# -*- encoding: utf-8 -*-
"""使用线程池实现光标旋转动画
也就是文本式旋转指针（由 ASCII 字符 "|/-\" 构成的动画旋转指）
"""

import itertools
import sys
import threading
import time


class Signal:
    """信号灯，给线程发送stop的信号"""
    go = True


def spin(msg, signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))  # 退格键\x08删除屏幕上面的字符
        time.sleep(.1)
        if not signal.go:
            break


def slow_function():
    # 假装等待I/O一段时间
    time.sleep(3)
    return 42


def supervisor():
    signal = Signal()
    spinner = threading.Thread(target=spin, args=('thinking!', signal))
    print('spinner object:', spinner)
    spinner.start()
    result = slow_function()
    signal.go = False
    spinner.join()
    return result


def main():
    result = supervisor()
    print('Answer:', result)


if __name__ == '__main__':
    main()
