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

# Consume Callback
def callback(ch, method, properties, body):
    print("%r:%r" % (method.routing_key, body))
    

while 1:
    try:
        # Parse input (look in helpers.py)
        mongo_insert = helpers.parse_input(input("Please input your command:"))
        
        # print checkpoint 2
        helpers.print_checkpoint(2, 'Store Command in MongoDB instance', mongo_insert)
        
        # insert to mongo database
        db.utilization.insert(mongo_insert)
        
        # Do action
        if mongo_insert['Action'] == 'p':
            # produce RabbitMQ message
            channel.basic_publish(exchange = mongo_insert['Place'],
                                  routing_key = mongo_insert['Subject'],
                                  body=mongo_insert['Message'])
            helpers.print_checkpoint(3, 'Sent produce type message to rabbitMQ - Queue', mongo_insert['Subject'])
        elif mongo_insert['Action'] == 'c':
            # consume RabitMQ message
            channel.basic_consume(callback,
                                  queue=mongo_insert['Subject'],
                                  no_ack=True)
            helpers.print_checkpoint(3, 'Output from queue consumption via callback', '')
            try:
                channel.start_consuming()
            except KeyboardInterrupt:
                channel.stop_consuming()
    except Exception as e:
        print(e)