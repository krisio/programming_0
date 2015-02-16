n1 = input("Enter the first number")
n2 = input("Enter the second number")

n1 = int(n1)
n2 = int(n2)

last_d1 = n1%10
last_d2 = n2%10


if last_d1>last_d2:
    print("Bigger last digit has: "+str(n1))
elif last_d1<last_d2:
    print("Bigger last digit has: "+str(n2))
else:
    if n1>n2:
        print("Equal digits, the bigger numer is: "+str(n1))
    else:
         print("Equal digits, the bigger numer is: "+str(n2))
