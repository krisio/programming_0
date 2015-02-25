def reverse_int(n):
    rev_num = 0

    while n != 0:
        d = n % 10

        rev_num = rev_num * 10 + d

        n = n // 10
        
    return rev_num

def sum_digits(n):
    tot_sum = 0

    while n != 0:
            d = n % 10
            tot_sum += d
            n = n // 10
    return tot_sum

def product_digits(n):
    tot_prod = 1

    while n!= 0:
        d = n % 10
        tot_prod = tot_prod * d
        n = n // 10
    return tot_prod
