#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 11:42:14 2020

@author: adamrankin
"""

#
# imports
#
import time

#
# Statics that won't change for use in this project
#
actions = ['p', 'c']

#dictionary of exchanges and related queues
exchanges = {'Squires': ['Food', 'Meetings', 'Rooms'],
             'Goodwin': ['Classrooms', 'Auditorium'],
             'Library': ['Noise', 'Seating', 'Wishes']}

# team number
team_number = '19'

#
# Method to print checkpopints based on a description
#
def print_checkpoint(num, des, data):
    output = []
    output.append('[Checkpoint 0' + str(num))
    output.append(str(time.time()) + ']')
    output.append(des + ':')
    output.append(str(data))
    print (' '.join(output))
    return

#
# Parses command input and checks for errors, returns in mongo insert form
#
def parse_input(command):
    try:
        #parse out command
        action = command.split(':')[0]
        exchange = command.split(':')[1].split('+')[0]
        queue = command.split(' ')[0].split('+')[1]
        message = ' '.join(command.split(' ')[1:])
        
        # Print checkpoint 1
        print_checkpoint(1, 'Message Captured', message)
    except:
        raise Exception('Error: Invalid command Format. Command format should follow action:exchange+queue message')
    
    # Error handling
    if action not in actions:
        raise Exception("Error: Invalid action. Action should be 'p' or 'c'.")
    elif exchange not in exchanges.keys():
        raise Exception("Error: Exchange {} not found.".format(exchange))    
    elif queue not in exchanges[exchange]:
        raise Exception("Error: Queue {} not found in ".format(queue) + exchange)
    
    # Build mongo insert
    mongo_insert = {
        'Action': action,
        'Place': exchange,
        'MsgID': ''.join([team_number, '$', str(time.time())]),
        'Subject': queue,
        'Message': message }
    
    return mongo_insert
    
    
    
    
    
    
    
    
    
    
    
    