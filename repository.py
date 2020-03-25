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
channel.exchange_declare(exchange='Squires')
channel.exchange_declare(exchange='Goodwin')
channel.exchange_declare(exchange='Library')

# Message Queues
channel.queue_declare(queue='Food')
channel.queue_declare(queue='Meetings')
channel.queue_declare(queue='Rooms')
channel.queue_declare(queue='Classrooms')
channel.queue_declare(queue='Auditorium')
channel.queue_declare(queue='Noise')
channel.queue_declare(queue='Seating')
channel.queue_declare(queue='Wishes')

# Bind queues to Exchanges
channel.queue_bind(exchange='Squires',
                   queue='Food',
                   routing_key='Food')
channel.queue_bind(exchange='Squires',
                   queue='Meetings',
                   routing_key='Meetings')
channel.queue_bind(exchange='Squires',
                   queue='Rooms',
                   routing_key='Rooms')
channel.queue_bind(exchange='Goodwin',
                   queue='Classrooms',
                   routing_key='Classrooms')
channel.queue_bind(exchange='Goodwin',
                   queue='Auditorium',
                   routing_key='Auditorium')
channel.queue_bind(exchange='Library',
                   queue='Noise',
                   routing_key='Noise')
channel.queue_bind(exchange='Library',
                   queue='Seating',
                   routing_key='Seating')
channel.queue_bind(exchange='Library',
                   queue='Wishes',
                   routing_key='Wishes')



while 1:
    try:
        # Parse input (look in helpers.py)
        mongo_insert = helpers.parse_input(input("Please input your command:"))
        
        # print checkpoint 2
        helpers.print_checkpoint(2, 'Store Command in MongoDB instance', mongo_insert)
        
        # insert to mongo database
        db.utilization.insert(mongo_insert)
        
        # publish to RabbitMQ message queue
        channel.basic_publish(exchange = mongo_insert['Place'],
                              routing_key = mongo_insert['Subject'],
                              body=mongo_insert['Message'])
        
    except Exception as e:
       print(e)