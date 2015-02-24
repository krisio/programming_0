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

def n_perfect(c):
    perfects = []
    n = 6
    
    while True:
        if is_perfect(n):
            perfects = perfects +  [n]
            c = c - 1
        if c == 0:
            break
        n += 1
    return perfects



c = input("Enter c: ")
c = int(c)
print("First " + str(c) + " perfects are:")
print(n_perfect(c))
