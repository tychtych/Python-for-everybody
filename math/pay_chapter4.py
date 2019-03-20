def computepay (hrs, r):
    if hrs <= 40:
        pay = hrs * r
        return pay
    elif hrs > 40:
        pay = 40 * r + (hrs-40) * 1.5 * r
        return pay

hrs = input("Enter Hours:")
h = float(hrs)
rate = input ("Enter Rate:")
r = float(rate)
p = computepay(h, r)
print (p)