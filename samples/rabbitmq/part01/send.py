#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
desc: sample

:copyright: (c) 2017 by Xiong Neng.
:license: MIT, see LICENSE for more details.
"""

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.217.161', port=5673))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()


