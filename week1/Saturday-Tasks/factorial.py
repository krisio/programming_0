n = input("Enter a number to factorial: ")
n = int(n)

result = 1
start = 1


if n >0:
    while start<=n:
        result = start*result
        start+=1
else:
    result = 1
print("The "+ str(n) + " factorial is: "+ str(result))
