hours = raw_input ("How many hours did you work?")
try:
    if hours <= 40:
        pay = str(int(hours)* 10)
        print 'your pay is ' + pay
    if hours > 40:
        pay = str((40*10)+((int(hours)s - 40)*15))
        print 'your pay is ' + pay
except:
    print "Error, please enter numeric input"
