#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 09:01:44 2020

@author: adamrankin
"""

#
# Import
#
import pika
import pickle

nums = [1, 2, 10, 11]


#
# Con
#
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='Adder')
channel.basic_publish(exchange='',                      
                      routing_key='Adder',                      
                      body=pickle.dumps(nums))
print (" [x] Sent list: " + str(nums) )
connection.close() 
