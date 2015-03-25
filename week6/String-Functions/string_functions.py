def change_at(index, ch, string):
    result = ""
    n = len(string)

    for str_index in range(0, n):
        if str_index == index:
            result += ch
        else:
            result += string[str_index]

    return result

def string_to_char_list(string):
    result = []

    for ch in string:
        result += [ch]

    return result


def char_list_to_string(char_list):
    result = ""

    for ch in char_list:
        result += ch

    return result


def change_string(index, ch, string):
    char_list = string_to_char_list(string)

    char_list[index] = ch

    return char_list_to_string(char_list)

def str_reverse(string):
    n_str = ""
    end = len(string)
    for i in range(0, end):

        n_str += string[end - 1 - i]
    return n_str

def join(delimiter, items):
    n_list = ""
    end = len(items)-1
    

    for i in range(0, end):
        item = items[i]
        n_list = n_list + item + delimiter

    n_list += items[end]
 
    return n_list

def tail(items):
    result = []

    for index in range(1, len(items)):
        item = items[index]
        result += [item]

    return result

def str_drop(n, string):
    result = ""

    for index in range(n, len(string)):
        result += string[index]

    return result

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

def trim_left(string):
    while startswith(" ", string):
        string = str_drop(1, string)
    return string

def trim_right(string):
    return str_reverse(trim_left(str_reverse(string)))

def trim(string):
    result = trim_left(string)
    result = trim_right(result)
    return result

        
