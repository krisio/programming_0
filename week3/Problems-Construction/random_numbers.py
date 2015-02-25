from random import randint

def generate_random_list(n, start, end):

    rand_nums = []

    while n != 0:
        rand = randint(start, end)
        rand_nums = rand_nums + [rand]
        n -= 1
    return rand_nums
        
