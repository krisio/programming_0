def sum_row(matrix, index):
    return sum(matrix[index])
 
 
def sum_col(matrix, index):
    result = 0
    for row in matrix:
        result += row[index]
 
    return result

def main_diag(matrix):
    count = 0

    for i in range(0, len(matrix)):
        count += matrix[i][i]
    return count

def secondary_diag(matrix):
    count = 0

    for i in range(len(matrix)-1,-1,-1):
        count += matrix[len(matrix)-1-i][i]
    return count

def magic(square):
    row_and_col = False
    is_magic = False

    for i in range (0,len(square)):
        

        if sum_row(square,i) == sum_col(square,i) == main_diag(square) == secondary_diag(square):
            is_magic = True

    return is_magic
        
            
