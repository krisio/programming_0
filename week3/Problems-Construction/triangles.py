import math

def is_triangle(a, b, c):

    triangle = False

    if a<c+b and a>b-c and a>c-b and b<a+c and b>a-c and b>c-a and c<a+b and c>a-b and c>b-a:
        triangle = True
    return triangle

def area(a, b, c):
    
    p = (a + b + c) / 2

    return math.sqrt((p - a)*(p - b)*(p - c))

def is_pythagorean(a, b, c):
    is_pyth = False

    if (a ** 2) + (b ** 2) == c ** 2:
        is_pyth = True
    return is_pyth

def max_area(triangles):

    max_tr = triangles[0]

    a = max_tr[0]
    b = max_tr[1]
    c = max_tr[2]
    
    max_ar = area(a,b,c)

    for triangle in triangles:
        a = triangle[0]
        b = triangle[1]
        c = triangle[2]

        c_ar = area(a,b,c)

        if max_ar < c_ar:
            max_tr = triangle
            max_ar = c_ar

    return max_tr
#triangles = [[2,3,4], [4,5,6], [6,7,8]]
