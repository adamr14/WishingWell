#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#import pymongo
import helpers
import pymongo

# Initialization
db = pymongo.MongoClient().test


while 1:
    try:
        # Parse input (look in helpers.py)
        mongo_insert = helpers.parse_input(input("Please input your command:"))
        
        print (mongo_insert)
        # insert to mongo database
        db.utilization.insert(mongo_insert)
        
    except Exception as e:
       print(e)