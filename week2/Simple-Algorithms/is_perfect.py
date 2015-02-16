n = input("Enter n:")
n = int(n)

divisors = []
div_sum = 0
is_perfect = True

beg = 1

while beg<n:
    if n%beg==0:
        divisors = divisors + [beg]
    beg+=1
for divisor in divisors:
    div_sum+=divisor
    
if n != div_sum:
    is_perfect = False


if is_perfect:
    print(str(n) + " is perfect")
else:
    print(str(n) + " is not perfect")
