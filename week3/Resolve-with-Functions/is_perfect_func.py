def divisors(n):

    divisors = []
    beg = 1
    while beg < n:
        if n % beg == 0:
            divisors = divisors + [beg]
        beg += 1
    return divisors

def sum_ints(nums):
    summ = 0
    for num in nums:
        summ += num
    return summ

def sum_divisors(n):
    return sum_ints(divisors(n))

def is_perfect(n):
    
    is_perfect = True
    
    if sum_divisors(n) != n:
        is_perfect = False
    return is_perfect

n = input("Enter n:")
n = int(n)

if is_perfect(n):
    print(str(n) + " is perfect")
else:
    print(str(n) + " is not perfect")
