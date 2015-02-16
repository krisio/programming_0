n = input("Enter n :")
n = int(n)

n_l = n - 2
n_r = n + 2

is_prime = True
is_l_prime = True
is_r_prime = True
start = 2

while start < n:
    if n% start == 0:
        is_prime = False
        break
    start = start + 1
start = 2
while start < n_l:
    if n_l % start == 0:
        is_l_prime = False
        break
    start = start + 1
start = 2
while start < n_r:
    if n_r % start == 0:
        is_r_prime = False
        break
    start = start + 1

if is_prime and is_l_prime and is_r_prime:
    print("Twin primes of " +str(n)+ " are:")
    print(n_l, n_r)
elif is_prime:
    print(str(n)+ " is prime")
    print("But " + str(n_l) + " " +  str(n_r) + " are not primes")
elif is_prime and is_l_prime:
    print(str(n) + " and its left twin " +str(n_l) + " are prime")
    print("But its right twin " + str(n_r) + " is not prime")
elif is_prime and is_r_prime:
    print(str(n) + " and its right twin " +str(n_r) + " are prime")
    print("But its left twin " + str(n_l) + " is not prime")
else:
    print("The number " + str(n) + " is not prime")
