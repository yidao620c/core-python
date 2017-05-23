#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
desc: sample

:copyright: (c) 2017 by Xiong Neng.
:license: MIT, see LICENSE for more details.
"""
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.217.161', port=5673))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         type='topic')

routing_key = 'disk.error'
message = '[disk.info] Hello World!'
channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_key,
                      body=message)
print(" [x] Sent %r:%r" % (routing_key, message))

routing_key = 'disk.warning'
message = '[disk.warning] Hello World!'
channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_key,
                      body=message)
print(" [x] Sent %r:%r" % (routing_key, message))


routing_key = 'test.error'
message = '[test.error] Hello World!'
channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_key,
                      body=message)
print(" [x] Sent %r:%r" % (routing_key, message))


connection.close()

