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

def to_digits(n):
    digits = []
    
    while n != 0:
        digit = n % 10
        digits = [digit] + digits

        n = n // 10
    return digits

n = input("Enter n :")
n = int(n)

f_digits = to_digits(n)

has_prime = False

for digit in f_digits:
    if is_prime(digit):
        has_prime = True

if has_prime:
    print("It has prime digit")
else:
    print("It has not a prime digit")
    
