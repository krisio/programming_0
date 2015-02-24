def squared(a):
    a ** 2
    return a

def fact(b):
    beg = 1
    result = 1
    while beg <= b:
        result = beg*result
        beg+=1
    return result

def count_elements(c):
    return len(c)

def member(x, xs):
    is_member = False
    for member in xs:
        if x == member:
            is_member = True
    return is_member

def grades_that_pass(students, grades, limit):
    
    passed = []
    beg = 0
    end = len(grades)
    
    while beg < end:
        if grades[beg] >= limit:
            student = students[beg]
            passed = passed + [student]
        beg+=1
    return passed

        
    
