#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
desc: sample

:copyright: (c) 2017 by Xiong Neng.
:license: MIT, see LICENSE for more details.
"""
import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.217.161', port=5673))
channel = connection.channel()

channel.queue_declare(queue='task_queue')

messages = ['python new_task.py First message.',
            'python new_task.py Second message..',
            'python new_task.py Third message...',
            'python new_task.py Fourth message....',
            'python new_task.py Fifth message.....',
            'python new_task.py Sixth message......']
for m in messages:
    channel.basic_publish(exchange='',
                          routing_key='task_queue',
                          body=m,
                          properties=pika.BasicProperties(
                              delivery_mode=2,  # make message persistent
                          ))
    print(" [x] Sent %r" % m)

connection.close()