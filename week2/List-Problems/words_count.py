word = input("Enter a word: ")
n = input("Size: ")
n = int(n)
words = []
start = 0
end = n
while start<end:
    wordin = input("word?: ")
    words = words + [wordin]
    start+=1
print(words)

beg = 0
count = 0
while beg<len(words):
    if word == words[beg]:
        count+=1
    beg+=1
print(word+ " is found " +str(count)+" times")
