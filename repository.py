#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#import pymongo
import helpers


while 1:
    #try:
    mongo_insert = helpers.parse_input(input("Please input your command:"))
    print (mongo_insert)
    #except Exception as e:
       #print(e)