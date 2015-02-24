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

n = input("Enter n :")
n = int(n)

n_l = n - 2
n_r = n + 2

is_n_prime = is_prime(n)
is_l_prime = is_prime(n_l)
is_r_prime = is_prime(n_r)

if is_n_prime and is_l_prime and is_r_prime:
    print("Twin primes of " +str(n)+ " are:")
    print(n_l, n_r)
elif is_n_prime:
    print(str(n)+ " is prime")
    print("But " + str(n_l) + " " +  str(n_r) + " are not primes")
elif is_n_prime and is_l_prime:
    print(str(n) + " and its left twin " +str(n_l) + " are prime")
    print("But its right twin " + str(n_r) + " is not prime")
elif is_n_prime and is_r_prime:
    print(str(n) + " and its right twin " +str(n_r) + " are prime")
    print("But its left twin " + str(n_l) + " is not prime")
else:
    print("The number " + str(n) + " is not prime")
