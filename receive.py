#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 09:09:29 2020

@author: adamrankin
"""
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters( host='localhost'))
channel = connection.channel() 
channel.queue_declare(queue='hello')
print (' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):       
    print (" [x] Received %r" % (body,))
    
channel.basic_consume(callback,queue='hello',no_ack=True)
channel.start_consuming()