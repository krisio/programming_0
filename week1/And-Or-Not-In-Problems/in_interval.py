a = input("Enter the beg of interval:")
a = int(a)
b = input("Enter the end of inrerval:")
b = int(b)
x = input("Enter nuber to check:")
x = int(x)

if x==a:
    print("The number is equal to the lower bound of the interval")
elif x==b:
    print("The number is equal to the upper bound of the interval")
elif x>a and x<b:
    print("The number is in the interval")
elif x<a:
    print("The number is outside the interval, x < a")
elif x>b:
    print("The number is outside the interval, x > b")
