h = raw_input ("Enter hours:")
r = raw_input ("Enter rate of pay:")
if h <= 40:
    pay = float(h) * float(r)
    print pay
if h > 40:
    pay = ((float(h) - 40) * (float(r)*1.5)) + (40 * float(r))
    print pay