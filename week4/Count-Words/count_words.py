def count_words(words):
    counted = {}
    unique_words = []
    ch = 0

    for word in words:
        if word not in unique_words:
            unique_words = unique_words + [word]
    word_freq = []
    
    for word in unique_words:
        word_freq += [words.count(word)]

    for word in unique_words:
        if ch < len(word_freq):
            counted[word] = word_freq[ch]
        ch += 1
            
    return counted

print(count_words(["are","iivan","are","go","go","stoio","are"]))
