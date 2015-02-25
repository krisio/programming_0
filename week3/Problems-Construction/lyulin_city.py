
def enter_list(n):
    count = 1
    floors = []

    while count <= n:
        floor = input("Enter floor: ")
        floor = int(floor)

        floors = [floor] + floors

        count += 1
    return floors

def seen_blocks(n):
    seen = 1
    beg = 0
    end = len(n)
    highest = n[0]

    for bl in n:
        if bl < highest:
            seen += 1
            highest = bl

    return seen

        
n = input("Enter the number of blocks: ")
n = int(n)

print(seen_blocks(enter_list(n)))


