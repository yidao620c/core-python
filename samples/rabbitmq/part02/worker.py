#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
desc: sample

:copyright: (c) 2017 by Xiong Neng.
:license: MIT, see LICENSE for more details.
"""
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.217.161', port=5673))
channel = connection.channel()

channel.queue_declare(queue='task_queue')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='task_queue')

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

