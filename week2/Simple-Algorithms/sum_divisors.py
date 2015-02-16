n = input("Enter n:")
n = int(n)

divisors = []
div_sum = 0

beg = 1

while beg<n:
    if n%beg==0:
        divisors = divisors + [beg]
    beg+=1
for divisor in divisors:
    div_sum+=divisor
    
print("The sum of  the divisors of " + str(n) + " are: ")
print(div_sum)
