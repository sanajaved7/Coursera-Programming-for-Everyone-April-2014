# -*- coding: utf-8 -*-
"""
Created on Sun Jun  8 22:22:01 2014

@author: sanajaved
"""
count = 0
fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
    if line.startswith ('From '):
        x = line.split()
        print x[1]
        count = count + 1
    else:
        continue
print "There were", str(count), "lines in the file with From as the first word"
#print "There were", count, "lines
#if len(fname) < 1 : 
   # fname = "mbox-short.txt"