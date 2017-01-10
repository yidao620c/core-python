#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
模块，包，函数，类，对象的导入以及各自拥有的属性
"""
__author__ = "Xiong Neng"

if __name__ == '__main__':
    """
    # samples/
    #     __init__.py   (定义cool()函数)
    #     main.py       (定义aa()函数和User类)
    """

    # aa是一个模块函数
    from samples.main import aa
    print("type={}".format(type(aa)))
    # AttributeError: 'function' object has no attribute '__package__'
    # print("aa.__package__={}".format(aa.__package__))
    print("aa.__module__={}".format(aa.__module__))
    print("aa.__name__={}".format(aa.__name__))
    # AttributeError: 'function' object has no attribute '__file__'
    # print("aa.__file__={}".format(aa.__file__))
    print('----------------------------------------------------')

    # main是一个模块
    import samples.main as main
    print("type={}".format(type(main)))
    print("init.__package__={}".format(main.__package__))
    # AttributeError: 'module' object has no attribute '__module__'
    # print("init.__module__={}".format(main.__module__))
    print("init.__name__={}".format(main.__name__))
    print("init.__file__={}".format(main.__file__))
    print('----------------------------------------------------')

    # samples是一个模块，同时也是一个包
    import samples
    print("type={}".format(type(samples)))
    print("samples.__package__={}".format(samples.__package__))
    # AttributeError: 'module' object has no attribute '__module__'
    # print("samples.__module__={}".format(samples.__module__))
    print("samples.__name__={}".format(samples.__name__))
    print("samples.__file__={}".format(samples.__file__))
    print('----------------------------------------------------')

    # 导入包samples的__init__模块看看
    import samples.__init__ as sample_init
    print("type={}".format(type(sample_init)))
    print("sample_init.__package__={}".format(sample_init.__package__))
    # AttributeError: 'module' object has no attribute '__module__'
    # print("sample_init.__module__={}".format(sample_init.__module__))
    print("sample_init.__name__={}".format(sample_init.__name__))
    print("sample_init.__file__={}".format(sample_init.__file__))
    print('----------------------------------------------------')

    # 最后打印samples和sample_init的dir()，看看是否不一样
    print(dir(samples))  # 多了__init__，__path__，main这三个属性
    print(dir(sample_init))
    print('----------------------------------------------------')

    # 类的导入
    from samples.main import User
    print("type={}".format(type(User)))
    # AttributeError: type object 'User' has no attribute '__package__'
    # print("User.__package__={}".format(User.__package__))
    print("User.__module__={}".format(User.__module__))
    print("User.__name__={}".format(User.__name__))
    # AttributeError: type object 'User' has no attribute '__file__'
    # print("User.__file__={}".format(User.__file__))

    print('----------------------------------------------------')
    # 对象
    user = User("Jason")
    print("type={}".format(type(user)))
    # AttributeError: 'User' object has no attribute '__package__'
    # print("user.__package__={}".format(user.__package__))
    print("user.__module__={}".format(user.__module__))
    # AttributeError: 'User' object has no attribute '__name__'
    # print("user.__name__={}".format(user.__name__))
    # AttributeError: 'User' object has no attribute '__file__'
    # print("user.__file__={}".format(user.__file__))

    print('----------------------------------------------------')

