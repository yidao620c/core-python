#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
模块，包，函数的导入以及各自拥有的属性
"""
__author__ = "Xiong Neng"

if __name__ == '__main__':
    # samples/
    #     __init__.py   (定义cool()函数)
    #     main.py       (定义aa()函数)
    from samples.main import aa
    # aa是一个模块函数
    # AttributeError: 'function' object has no attribute '__package__'
    # print("aa.__package__={}".format(aa.__package__))
    print("aa.__module__={}".format(aa.__module__))
    print("aa.__name__={}".format(aa.__name__))
    # AttributeError: 'function' object has no attribute '__file__'
    # print("aa.__file__={}".format(aa.__file__))

    # main是一个模块
    import samples.main as main
    print("init.__package__={}".format(main.__package__))
    # AttributeError: 'module' object has no attribute '__module__'
    # print("init.__module__={}".format(main.__module__))
    print("init.__name__={}".format(main.__name__))
    print("init.__file__={}".format(main.__file__))

    # samples是一个模块，同时也是一个包
    import samples
    print("samples.__package__={}".format(samples.__package__))
    # AttributeError: 'module' object has no attribute '__module__'
    # print("samples.__module__={}".format(samples.__module__))
    print("samples.__name__={}".format(samples.__name__))
    print("samples.__file__={}".format(samples.__file__))

    # 导入包samples的__init__模块看看
    import samples.__init__ as sample_init
    print("sample_init.__package__={}".format(sample_init.__package__))
    # AttributeError: 'module' object has no attribute '__module__'
    # print("sample_init.__module__={}".format(sample_init.__module__))
    print("sample_init.__name__={}".format(sample_init.__name__))
    print("sample_init.__file__={}".format(sample_init.__file__))

    # 最后打印samples和sample_init的dir()，看看是否不一样
    print(dir(samples))  # 多了__init__，__path__，main这三个属性
    print(dir(sample_init))

