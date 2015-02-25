def travel_cost(travels):
    ticket = 1
    one_line = 23
    all_lines = 50
    cost = 0

    for travel in travels:
        if travel <= one_line:
            cost = cost + travel * ticket
        else:
            cost = cost + one_line

        if cost >= all_lines:
            cost = all_lines
    return cost

