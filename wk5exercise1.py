count = 0
total = 0
things = []

while True:
    number = raw_input('Enter a number:')
    
    if number == 'done':
        break    
    
    try:
        dog = int(number)
    
        things.append (dog)
        
    except:
        print 'Invalid input'
    
    
print "Number is:"
print number
print "things is:"
print things
      
for thing in things:
    count = float(count) + 1
    total = total + thing        
print total, count, (total/count)