def count_zero_neighbours(numbers):

    end = len(numbers)
    c = 0
    i = 0

    for number in numbers:

        if i < end -1:
            
            neigh = numbers[i + 1]
        
            if neigh + number == 0:
                c += 1
        i += 1

    return c

