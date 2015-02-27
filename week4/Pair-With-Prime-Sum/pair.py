def is_prime(n):
    is_prime = True
    beg = 2

    if n == 1:
        is_prime = False
    while beg < n:
        if n % beg == 0:
            is_prime = False
            break
        beg = beg + 1
    return is_prime


def prime_pair(numbers):

    has_prime_sum_pair = False

    for i in range (0, len(numbers)):
        for j in range (i, len(numbers)):

            firstnum = numbers[i]
            secondnum = numbers[j]

            summ = firstnum + secondnum

            if is_prime(summ):
                has_prime_sum_pair = True
    return has_prime_sum_pair
