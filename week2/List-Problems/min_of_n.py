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
smallest = 20000000

while beg<len(numbers):
    if numbers[beg]<smallest:
        smallest = numbers[beg]
    beg+=1
print("The smallest number from the list is " +str(smallest))
