#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#import pymongo
import helpers
from pymongo import MongoClient

# Initialization
client = MongoClient()


while 1:
    try:
        # Parse input (look in helpers.py)
        mongo_insert = helpers.parse_input(input("Please input your command:"))
        
        # insert to mongo database
        
    except Exception as e:
       print(e)