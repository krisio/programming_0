def change_at(index, ch, string):
    result = ""
    n = len(string)

    for str_index in range(0, n):
        if str_index == index:
            result += ch
        else:
            result += string[str_index]

    return result

def str_reverse(string):
    n_str = ""
    end = len(string)
    for i in range(0, end):

        n_str += string[end - 1 - i]
    return n_str

def startswith(search, string):

    starts = False
    end = len(search)

    for i in range(0, end):

        if search[i] != string[i]:
            break
        else:
            starts = True
    return starts

def endswith(search, string):

    ends = False
    search  = str_reverse(search)
    string = str_reverse(string)
    
    end = len(search)

    for i in range(0, end):

        if search[i] != string[i]:
            break
        else:
            ends = True
    return ends


        
