n = input("Enter your number: ")
n = int(n)

digits = []

while n != 0:
    digit = n % 10
    digits = [digit] + digits
    n = n // 10
print("List of digits is: " + str(digits))
n = 0
for digit in digits:
    n = n * 10 + digit
print("Number is " + str(n))
