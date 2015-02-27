def count_zero_pairs(numbers):
    c = 0
    for i in range (0, len(numbers)):
        for j in range (i, len(numbers)):

            firstnum = numbers[i]
            secondnum = numbers[j]

            if firstnum + secondnum == 0:
                c += 1
    return c



                
        
