# -*- coding: utf-8 -*-

fname = raw_input("Enter file name: ")
fh = open(fname)
lst = []
for line in fh:
    line = line.split()
    for word in line:
        if word in lst:
            continue
        else:
            lst.append(word)
lst.sort()
print lst
#print 
# print line.rstrip()
