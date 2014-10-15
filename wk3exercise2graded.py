s = raw_input ("Enter score:")
fs = float (s)
if fs > 0.9 and < 1:
    print "A"
elif fs >= 0.8:
    print "B"
elif fs >= 0.7:
    print "C"
elif fs >= 0.6:
    print "D"
elif fs < 0.6:
    print "F"
else: 
    print "Score out of range"