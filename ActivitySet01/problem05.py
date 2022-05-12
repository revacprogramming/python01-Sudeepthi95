def computepay(h, r):
    if h<=40:
        p=h*r
    else:
        p=(40*r)+(h-40)*1.5*r
    return p

hrs = float(input("Enter Hours:"))
rate = float(input("Enter the Rate:"))
p = computepay(hrs,rate)
print("Pay", p)