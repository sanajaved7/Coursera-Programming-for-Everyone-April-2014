fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
lists = []
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"): 
        col = line.find(':')
        end = len(line)
        num = line[col+1:end]
        r = float(num)
        lists.append(r)
        count = count + 1
x = sum(lists)/count
print 'Average spam confidence: ' + str(x) 