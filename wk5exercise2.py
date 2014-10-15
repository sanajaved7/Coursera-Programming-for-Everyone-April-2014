things = []
mx = 0
mn  = 100
while True:
    number = raw_input('Enter a number:')
    
    if number == 'done':
        break    
    
    try:
        dog = int(number)
    
        things.append (dog)
        
    except:
        print 'Invalid input'
        
for thing in things:
    if thing > mx:
        mx = thing      
print 'Maximum is ' + str(mx)

for thing in things:
    if thing < mn:
        mn = thing
print 'Minimum is ' + str(mn)