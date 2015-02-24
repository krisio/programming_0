def divisors(n):

    divisors = []
    beg = 1
    while beg < n:
        if n % beg == 0:
            divisors = divisors + [beg]
        beg += 1
    return divisors

n = input("Enter n:")
n = int(n)

print("The divisors of " + str(n) + " are: ")
print(divisors(n))
