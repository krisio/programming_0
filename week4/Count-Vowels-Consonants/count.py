def count_vowels_consonants(word):
    dictionary = {}
    vowels = "aeiouyAEIOUY"
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
    vow = 0
    cons = 0
    for char in word:
        if char in vowels:
            vow+=1
        if char in consonants:
            cons+=1
        
        dictionary["vowels"] = vow
        dictionary["consonants"] = cons
    return(dictionary)
print(dictionary)
