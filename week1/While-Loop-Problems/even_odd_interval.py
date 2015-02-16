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
    if start%2 == 0:
        print(str(start)+"- even")
    else:
        print(str(start)+"- odd")
    start+=1
    
