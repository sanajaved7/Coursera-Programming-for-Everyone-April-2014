# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 19:24:24 2014

@author: sanajaved
"""
dog = raw_input ("Enter file:")
x = open(dog)
dicto = dict()
for line in x:
    if line.startswith("From:"):
        words = line.split()        
        if words[1] not in dicto:
            dicto[words[1]] = 1
        else:
            dicto[words[1]] += 1

largest_email = None
largest_value= None
for email,value in dicto.items():
        if largest_email is None or value > largest_value:
            largest_email = email
            largest_value = value
print largest_email, largest_value