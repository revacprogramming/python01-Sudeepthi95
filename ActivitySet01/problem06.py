largest=None
smallest=None
while True:
    n=input("Enter a number\n")
    if n=="done":
        break
    try:
        num=int(n)
        if largest is None or largest<num:
            largest=num 
        if smallest is None or smallest>num:
             smallest=num        
    except:
        print("Invalid input")
        continue
print("Maximum is",largest)
print("Minimum is",smallest)