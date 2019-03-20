hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
pay = float(h) * float(r)
if h <= 40:
    float(h) * float(r)
    print(pay)
elif h > 40:
    adv_pay = 40 * r + (h-40) * 1.5 * r
    print(adv_pay)




