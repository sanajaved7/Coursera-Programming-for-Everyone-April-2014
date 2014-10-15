fname = raw_input("Enter file name: ")
fh = open(fname)
yo = fh.read().strip().upper()
'''yo = yo.strip()'''
print yo