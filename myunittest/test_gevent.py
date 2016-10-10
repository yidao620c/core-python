#!/opt/winstore/venv/bin/python
# -*-coding:utf-8-*-

import gevent
import gevent.monkey
gevent.monkey.patch_all()

from gevent.event import Event
from gevent.queue import Queue, Empty
from gevent.pool import Group, Pool
from gevent.local import local

import unittest
import random
import zerorpc
import logging
import sys
import urllib2
import json
import signal


def _get_log():
    _log = logging.getLogger(__name__)
    _log.setLevel(logging.DEBUG)
    # _handler = logging.FileHandler("./log.log")
    _handler = logging.StreamHandler(stream=sys.stderr)
    fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d ---> %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"
    formatter = logging.Formatter(fmt, datefmt)
    _handler.setFormatter(formatter)
    _log.addHandler(_handler)
    return _log

_log = _get_log()



class MyRpcInterface(object):

    def license_query(self):
        return "license_query"

    def op_mode_get(self):
        return "op_mode_get"

class Test(unittest.TestCase):

    def test_gevent1(self):
        """一个简单的上下文切换例子"""
        def foo():
            _log.info('Running in foo')
            gevent.sleep(0)
            _log.info('Explicit context switch to foo again')

        def bar():
            _log.info('Explicit context to bar')
            gevent.sleep(0)
            _log.info('Implicit context switch back to bar')

        gevent.joinall([
            gevent.spawn(foo),
            gevent.spawn(bar),
        ])
    
    def test_tasks(self):
        """同步和异步区别"""
        def task(pid):
            gevent.sleep(random.randint(0, 2) * 0.01)
            print('Task {0} done'.format(pid))
        
        def synchronous():
            for i in range(1, 10):
                task(i)

        def asynchronous():
            threads = [gevent.spawn(task, i) for i in xrange(10)]
            gevent.joinall(threads)
        
        _log.info('Synchronous:')
        synchronous()
        _log.info('Asynchronous:')
        asynchronous()
    
    # def test_url_fetch(self):
    #     """网络io的同步和异步"""
    #     def fetch(pid):
    #         response = urllib2.urlopen('https://jsonplaceholder.typicode.com/posts/1')
    #         result = response.read()
    #         json_result = json.loads(result)
    #         datetime = json_result['title']

    #         print('Process %s: %s' % (pid, datetime))
    #         return json_result['title']
        
    #     def synchronous():
    #         for i in range(1,10):
    #             fetch(i)

    #     def asynchronous():
    #         threads = []
    #         for i in range(1,10):
    #             threads.append(gevent.spawn(fetch, i))
    #         gevent.joinall(threads)

    #     _log.info('Synchronous1:')
    #     synchronous()
    #     _log.info('Asynchronous1:')
    #     asynchronous()

    def test_greenlet(self):
        """测试自己写的Greenlet协程子类"""
        class MyGreenlet(gevent.Greenlet):
            def __init__(self, message, n):
                super(MyGreenlet, self).__init__()
                self.message = message
                self.n = n

            def _run(self):
                print(self.message)
                gevent.sleep(self.n)
        
        g1 = MyGreenlet("Hi there111!", 1)
        g1.start()
        g2 = MyGreenlet("Hi there222!", 2)
        g2.start()
        gevent.joinall([g1, g2])

    # def test_shutdown(self):
    #     def run_forever():
    #         _log.info('run_forever start..')
    #         gevent.sleep(1000)
    #     gevent.signal(signal.SIGQUIT, gevent.kill)
    #     thread = gevent.spawn(run_forever)
    #     thread.join()

    def test_event(self):
        """测试通过event对象在多个协程之间通信"""
        evt = Event()

        def setter():
            '''After 3 seconds, wake all threads waiting on the value of evt'''
            _log.info('A: Hey wait for me, I have to do something')
            gevent.sleep(3)
            _log.info("Ok, I'm done")
            evt.set()

        def waiter():
            '''After 3 seconds the get call will unblock'''
            _log.info("I'll wait for you")
            evt.wait()  # blocking
            _log.info("It's about time")
        
        gevent.joinall([
            gevent.spawn(setter),
            gevent.spawn(waiter),
            gevent.spawn(waiter),
            gevent.spawn(waiter),
            gevent.spawn(waiter),
            gevent.spawn(waiter)
        ])

    def test_queue(self):
        """测试非阻塞和协程安全的Queue"""
        task_queue = Queue()

        def worker(name):
            while not task_queue.empty():
                task = task_queue.get()
                _log.info('Worker %s got task %s' % (name, task))
                gevent.sleep(0)

            _log.info('Quitting time!')

        def boss():
            for i in xrange(1,25):
                task_queue.put_nowait(i)

        gevent.spawn(boss).join()

        gevent.joinall([
            gevent.spawn(worker, 'steve'),
            gevent.spawn(worker, 'john'),
            gevent.spawn(worker, 'nancy'),
        ])

    def test_queue2(self):
        """测试队列有size现在，阻塞get/set，并带有超时时间"""
        _log.info('test_queue2222222222')
        task_queue = Queue(3)
        def worker(name):
            try:
                while True:
                    task = task_queue.get(timeout=1) # decrements queue size by 1
                    print('Worker %s got task %s' % (name, task))
                    gevent.sleep(0)
            except Empty:
                print('Quitting time!')

        def boss():
            """
            Boss will wait to hand out work until a individual worker is
            free since the maxsize of the task queue is 3.
            """

            for i in xrange(1,10):
                task_queue.put(i)
            print('Assigned all work in iteration 1')

            for i in xrange(10,20):
                task_queue.put(i)
            print('Assigned all work in iteration 2')

        gevent.joinall([
            gevent.spawn(boss),
            gevent.spawn(worker, 'steve'),
            gevent.spawn(worker, 'john'),
            gevent.spawn(worker, 'bob'),
        ])

    def test_group(self):
        def talk(msg):
            for i in xrange(3):
                print(msg)

        g1 = gevent.spawn(talk, 'bar')
        g2 = gevent.spawn(talk, 'foo')
        g3 = gevent.spawn(talk, 'fizz')

        group = Group()
        group.add(g1)
        group.add(g2)
        group.join()

        group.add(g3)
        group.join()

    def test_pool(self):
        """测试协程池"""
        class SocketPool(object):

            def __init__(self):
                self.pool = Pool(1000)
                self.pool.start()

            def listen(self, socket):
                while True:
                    socket.recv()

            def add_handler(self, socket):
                if self.pool.full():
                    raise Exception("At maximum pool size")
                else:
                    self.pool.spawn(self.listen, socket)

            def shutdown(self):
                self.pool.kill()

    def test_local(self):
        """
        线程局部变量
        很多集成了gevent的web框架将HTTP会话对象以线程局部变量的方式存储在gevent内
        """
        stash = local()
        def f1():
            stash.x = 1
            print(stash.x)

        def f2():
            stash.y = 2
            print(stash.y)

            try:
                stash.x
            except AttributeError:
                print("x is not local to f2")

        g1 = gevent.spawn(f1)
        g2 = gevent.spawn(f2)
        gevent.joinall([g1, g2])


if __name__ == '__main__':
    unittest.main()

