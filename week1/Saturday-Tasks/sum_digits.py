n = input("Enter number")

n = int(n)

tot_sum = 0

while n != 0:
    d = n%10
    tot_sum +=d
    n = n//10
print("The sum of number's digits is: "+str(tot_sum))
