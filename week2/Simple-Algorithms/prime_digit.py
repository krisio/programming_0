n = input("Enter n :")
n = int(n)

digits = []
primes = [2, 3, 5, 7]
has_prime = False

while n != 0:
    digit = n%10
    digits = [digit] + digits

    n = n//10
for prime in primes:   
    if prime in digits:
        has_prime = True
        
if has_prime:
    print("The number has a prime digit")
else:
    print("The number doesnt have a prime digit")

