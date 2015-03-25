
def str_reverse(string):
    result = ""

    for ch in string:
        result = ch + result

    return result



def is_string_palindrom(string):

    string = string.lower()

    clean_string = ""

    for ch in string:
        if not ch.isspace() and ch.isalnum():
            clean_string += ch
            

    if(clean_string == str_reverse(clean_string)):
        return True
    else:
        return False

print(is_string_palindrom("Az obi4am ma4 i boza"))
print(is_string_palindrom("A Toyota!"))
print(is_string_palindrom("bozaaa"))
print(is_string_palindrom(" kapak! "))
