#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 09:09:29 2020

@author: adamrankin
"""
import pika
import pickle

connection = pika.BlockingConnection(pika.ConnectionParameters( host='localhost'))
channel = connection.channel() 
channel.queue_declare(queue='Adder')
print (' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    nums = pickle.loads(body)     
    print (" [x] The sum of the list is" + str(sum(nums)))
    
channel.basic_consume(callback,queue='Adder',no_ack=True)
channel.start_consuming()