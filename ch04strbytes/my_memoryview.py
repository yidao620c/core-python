# -*- encoding: utf-8 -*-
"""
内存视图
常见支持内存视图操作的有bytes、bytearray、array.array，以及NumPy某些类型。
"""

if __name__ == '__main__':
    a = bytearray([0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16])
    v = memoryview(a)
    x = v[2:5]
    print(x.hex())
    a[3] = 0xee
    print(x.hex())
    pass
