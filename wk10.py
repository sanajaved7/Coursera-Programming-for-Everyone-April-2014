# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 19:24:24 2014

@author: sanajaved
"""
#read through mbox text
#figure out distribution by hour of day for each message
# pull hour from the "From" line - split the string a second time using  a colon
# once you have counts for each hour, print out counts and sort by hour
# auto grader doesn't support sorted() fxn

#dog = raw_input ("Enter file:")
dicto = dict()
x = open('mbox-short.txt')
for line in x:
    if line.startswith("From"):
        words = line.split()
        if len(words) > 2:
            s= words[5]
            #print s[:2]
            if s[:2] not in dicto:
                dicto [s[:2]] = 1
            else:
                dicto [s[:2]] += 1
t = dicto.items()
t.sort()
for k,v in t:
    print k,v