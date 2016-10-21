#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    Topic: sample

    Filter(logname)，只允许来自logname或其子日志的消息通过
    app.net是app的子日志

    消息传播propagate和分层记录器：消息会传播给父记录器
    log.propagate属性获取是否传播标志

"""
import logging
import logging.handlers as handlers
import logging.config as config

# 时间 | 日志级别 | 文件名 | 行号 | 进程ID | 消息体
fmt = "%(asctime)-15s [%(levelname)s] %(filename)s %(lineno)d %(process)d ===> %(message)s"
datefmt = "%Y-%m-%d %H:%M:%S"
formatter = logging.Formatter(fmt, datefmt)


class Logger(object):
    """ provides a memory-inexpensive logger.  a gotcha about python's builtin
    logger is that logger objects are never garbage collected.  if you create a
    thousand loggers with unique names, they'll sit there in memory until your
    script is done.  with sh, it's easy to create loggers with unique names if
    we want our loggers to include our command arguments.  for example, these
    are all unique loggers:

            ls -l
            ls -l /tmp
            ls /tmp

    so instead of creating unique loggers, and without sacrificing logging
    output, we use this class, which maintains as part of its state, the logging
    "context", which will be the very unique name.  this allows us to get a
    logger with a very general name, eg: "command", and have a unique name
    appended to it via the context, eg: "ls -l /tmp" """
    def __init__(self, name, context=None, logfile=None, level=logging.DEBUG):
        self.name = name
        if context:
            context = context.replace("%", "%%")
        self.context = context
        self.log = logging.getLogger(name)
        self.log.setLevel(level)
        # self.log.propagate = False  # 关闭传播属性
        _handler = logging.handlers.TimedRotatingFileHandler(logfile, when='D', interval=7)
        _handler.setFormatter(formatter)
        self.log.addHandler(_handler)

    def _format_msg(self, msg, *args):
        if self.context:
            msg = "%s: %s" % (self.context, msg)
        return msg % args

    def get_child(self, name, context):
        new_name = self.name + "." + name
        new_context = self.context + "." + context
        l = Logger(new_name, new_context)
        return l

    def debug(self, msg, *args):
        self.log.debug(self._format_msg(msg, *args))

    def info(self, msg, *args):
        self.log.info(self._format_msg(msg, *args))

    def warn(self, msg, *args):
        self.log.warn(self._format_msg(msg, *args))

    def error(self, msg, *args):
        self.log.error(self._format_msg(msg, *args))

    def exception(self, msg, *args):
        self.log.exception(self._format_msg(msg, *args))


class FilterFunc(logging.Filter):
    def __init__(self, name):
        super().__init__()
        self.funcname = name

    def filter(self, record):
        if record.funcName == self.funcname: return False


def my_log():
    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.FileHandler('message.log', 'a', 'utf-8')])
    # 模块基本用_，类级别用__
    _log = logging.getLogger('app.' + __name__)
    host = '10.0.0.175'
    port = 8080
    # 不要用 'xxxx' % (aa, bb)去手动格式化消息
    _log.error('error to connect to %s:%d', host, port)
    _log.addFilter(FilterFunc('foo'))  # 将忽略来自foo()函数的所有消息
    lgg = logging.getLogger('app.network.client')
    lgg.propagate = False  # 关闭传播属性
    lgg.error('do you see me?')  # 但是还是可以看到
    lgg.setLevel(logging.CRITICAL)
    lgg.error('now you see me?')
    logging.disable(logging.DEBUG)  # 全局关闭某个级别
    # 使用log配置文件，在main函数中执行一次即可
    config.fileConfig('applogcfg.ini')


if __name__ == '__main__':
    log = Logger(__name__, 'ls -l', logfile='D:/temp.log')
    log.info('11111111111111111111')
    log.debug('2222222222222222222222222222')
