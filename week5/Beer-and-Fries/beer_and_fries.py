def max_score(beers, fries):
    
    final_score = 0
    i = 0
    sorted_beers = sorted(beers, reverse = True)
    sorted_fries = sorted(fries, reverse = True)

    for i in range(0 , len(sorted_beers)):
        
            final_score = final_score + (sorted_beers[i]*sorted_fries[i])

    return final_score

