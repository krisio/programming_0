n = input("Enter n: ")
n = int(n)
first = 6

while True:
    div_sum = 0
    div = 1
    is_perfect = False

    while div < first:
        if first % div == 0:
            div_sum += div
        div += 1
    if div_sum == first:
        is_perfect = True
    if is_perfect:
        print(first)
        n = n - 1
    if n == 0:
        break
    first += 1
