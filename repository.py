#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Imports 
#
import helpers
import pymongo
import pika

#
# Initialization
#

# Mongo database
db = pymongo.MongoClient().test

# RabbitMQ Connections
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

# Exchanges
channel.exchange_declare(exchange='Squires',
                         type='direct')
channel.exchange_declare(exchange='Goodwin',
                         type='direct')
channel.exchange_declare(exchange='Library',
                         type='direct')

# Message Queues
channel.queue_declare(queue='Food')
channel.queue_declare(queue='Meetings')
channel.queue_declare(queue='Rooms')
channel.queue_declare(queue='Classrooms')
channel.queue_declare(queue='Auditorium')
channel.queue_declare(queue='Noise')
channel.queue_declare(queue='Seating')
channel.queue_declare(queue='Wishes')



while 1:
    try:
        # Parse input (look in helpers.py)
        mongo_insert = helpers.parse_input(input("Please input your command:"))
        
        # print checkpoint 2
        helpers.print_checkpoint(2, 'Store Command in MongoDB instance', mongo_insert)
        
        # insert to mongo database
        db.utilization.insert(mongo_insert)
        
    except Exception as e:
       print(e)