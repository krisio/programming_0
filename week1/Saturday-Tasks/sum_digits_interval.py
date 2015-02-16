n1 = input("Enter the first number")
n2 = input("Enter the second number")

n1 = int(n1)
n2 = int(n2)

if n1<n2:
    start=n1
    end=n2
else:
    start=n2
    end=n1
    

while start<=end:
    n = start
    tot_sum = 0

    while n != 0:
        d = n%10
        tot_sum +=d
        n = n//10
        
    print("The sum of "+ str(start)+ "'s digits is: "+str(tot_sum))
    start+=1
