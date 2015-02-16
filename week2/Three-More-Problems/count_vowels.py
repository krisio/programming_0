n = input("Enter a string to check for vowels: ")

counter = 0
vowels = "aeiouyAEIOUY"

for ch in n:
    if ch in vowels:
        counter+=1

print(counter)
