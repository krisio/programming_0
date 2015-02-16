n = input("Enter a number:")
n = int(n)

start = 1
tot_sum = 0

while start<=n:
    if start%2 == 0:
        tot_sum+=start

    start+=1
print("The sum of all evens is " + str(tot_sum))
