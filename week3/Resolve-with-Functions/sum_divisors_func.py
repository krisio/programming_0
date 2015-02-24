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

def div_sum(n):
    return sum_ints(divisors(n))

n = input("Enter n:")
n = int(n)
print("The sum of  the divisors of " + str(n) + " are: ")
print(div_sum(n))
