a = input("Enter number a:")
a = int(a)
b = input("Enter number b:")
b = int(b)

if a<b:
    start = a
    end = b
else:
    start = b
    end = a
    
while start<=end:
    print(start)
    start+=1
    
