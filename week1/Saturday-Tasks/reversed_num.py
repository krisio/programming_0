n = input("Enter a number: ")
n = int(n)

rev_num = 0

while n != 0:
    d = n%10

    rev_num = rev_num*10+d

    n = n//10
print("The reveresd num is:" + str(rev_num))

