n = input("Enter a number: ")
n = int(n)

orig_num = n
rev_num = 0

while n != 0:
    d = n%10

    rev_num = rev_num*10+d

    n = n//10
if orig_num == rev_num:
    print("The number "+ str(orig_num) + "is polidrom")
else:
    print("The number "+ str(orig_num) + "is not polidrom")

