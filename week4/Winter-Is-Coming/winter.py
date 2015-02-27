def winter_is_coming(seasons):

    is_winter_coming = False
    
    count = 0

    for season in seasons:
        if season != "winter":
            count += 1
        elif season == "winter":
            count = 0
        if count == 5:
            is_winter_coming = True
            
    return is_winter_coming

