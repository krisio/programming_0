def sublist(list1, list2):

    is_list = False
    
    for i in range(len(big)-len(small)+1):
        for j in range(len(small)):
            if big[i+j] != small[j]:
                break
        else:
            is_list = True
    return is_list


                

            
