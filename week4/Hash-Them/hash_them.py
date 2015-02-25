def hash_them(keys, values):

    hash_table = {}
    
    ch = 0
    
    for key in keys:
        
            if ch < len(values):
                
                hash_table[key] = values[ch]
            else:
                
                hash_table[key] = None
                
            ch+=1
                
    return hash_table




