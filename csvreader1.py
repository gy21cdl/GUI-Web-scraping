# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 18:27:32 2022

@author: clambert
"""
#Lines here happen before any data is processed
import csv
import matplotlib

def get_data():
    f = open('in.txt', newline='')
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    
    environment = []
    for row in reader: # A list of rows
        rowlist = []    
        for value in row: # A list of value
            rowlist.append(value)
            #print(value) # Floats
        environment.append(rowlist)
 
    f.close() # Don't close until you are done with the reader;
    # the data is read on request.
    return environment

