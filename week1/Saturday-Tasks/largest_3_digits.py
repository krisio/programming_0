n = input("Enter a 3-digit number: ")
n = int(n)

d1 = n//100
d2 = n//10-d1*10
d3 = n%10

print(d1, d2, d3)

l = d1

if d2 >= l and d2 >= d3:
    l = d2
if d3 >= l and d3 >= d2:
    l = d3
print("Largets digit: " + str(l))

s = d1
if d2 <= s and d2 <= d3:
    s = d2
if d3 <= s and d3 <= d2:
    s = d3
print("Smallest digit: " + str(s))

m = d3
if (l == d3 and s == d2) or (s == d3 and l == d2):
    m= d1
elif (l == d3 and s == d1) or (s == d3 and l == d1):
    m = d2
max_number = l * 100 + m * 10 + s
min_number = s * 100 + m * 10 + l
print("The largest num with these digits: " + str(max_number))
print("The smallest num with these digits: " + str(min_number))
