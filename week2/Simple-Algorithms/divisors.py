n = input("Enter n:")
n = int(n)

divisors = []

beg = 1

while beg<n:
    if n%beg==0:
        divisors = divisors + [beg]
    beg+=1
print("The divisors of " + str(n) + " are: ")
print(divisors)
