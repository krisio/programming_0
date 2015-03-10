def head(lst):
    return lst[0]

def last(lst):
    return lst[len(lst)-1]

def tail(lst):
    n_lst = []
    
    for i in range(1, len(lst)):
        n_lst = n_lst + [lst[i]]
        
    return n_lst
    
def equal_lists(lst1, lst2):
    are_equal = False

    if lst1 == [] and lst2 == []:
        are_equal = True
    
    if len(lst1) == len(lst2):

        for i in range(0, len(lst1)):

            if lst1[i] == lst2[i]:

                are_equal = True

    return are_equal

def count_item(n, lst):
    counter = 0
    
    for item in lst:
        if item == n:
            counter += 1

    return counter

def take(n, lst):
    n_lst = []

    if n > len(lst):
        return lst
    else:
        for i in range(0, n):
            n_lst = n_lst + [lst[i]]
        
        return n_lst
    

def drop(n, lst):
    n_lst = []
    
    for i in range(n, len(lst)):
        n_lst = n_lst + [lst[i]]
        
    return n_lst
