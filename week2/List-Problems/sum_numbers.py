n = input("How many numbers: ")
n = int(n)
numbers = []
start = 0
end = n
while start<end:
    number = input("Enter number: ")
    number = int(number)
    numbers = numbers + [number]
    start+=1
print(numbers)
beg = 0
summ = 0
while beg<len(numbers):
    summ+=numbers[beg]
    beg+=1
print("The sum of numers is: "+str(summ))
