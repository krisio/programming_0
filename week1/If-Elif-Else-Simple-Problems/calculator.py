a = input("Enter a:")
a = int(a)
b = input("Enter b:")
b = int(b)
oper = input("Operation:")
print("Result is:")

if oper == "+":
    print(a+b)
elif oper == "-":
    print(a-b)
elif oper == "*":
    print(a*b)
elif oper == "/":
    print (a/b)
else:
    print("No such operation")
