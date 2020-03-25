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