n = input("Enter a number to sum to:")
n = int(n)
start = 1
end = n
summ = 0

while start<=end:
    summ += start
    start += 1
print("The sum of all numbers in interval is:" + str(summ))
