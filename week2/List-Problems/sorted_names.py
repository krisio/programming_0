
n = input("Size: ")
n = int(n)
words = []
start = 0
end = n
while start<end:
    wordin = input("word?: ")
    words = words + [wordin]
    start+=1
for word in sorted(words):
    print(word)


