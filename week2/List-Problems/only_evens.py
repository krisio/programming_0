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
count = 0
for number in numbers:
    if number%2==0:
        count+=1
print("There are "+ str(count)+ " even numbers")
evens = []
beg = 0
num = 0
while beg<len(numbers):
    if numbers[beg]%2==0:
        
        evens = evens + [numbers[beg]]
    beg+=1
print(evens)
