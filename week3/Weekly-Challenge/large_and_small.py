
def to_digits(n):
    digits = []
    
    while n != 0:
        digit = n % 10
        digits = [digit] + digits

        n = n // 10
    return digits

def minimum_num(n):
    return sorted(n)

def maximum_num(n):
    return sorted(n , reverse = True)

def to_number(n):
    
    f_num = 0
    for dig in n:
        f_num = f_num * 10 + dig
    return f_num

n = input("Enter n: ")
n = int(n)

print("The maximal number is:")
print(to_number(maximum_num(to_digits(n))))

print("The minimal number is:")
print(to_number(minimum_num(to_digits(n))))

        
