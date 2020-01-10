
# Sudoku
[[5, 3, 4, 6, 7, 8, 9, 1, 2], [6, 7, 2, 1, 9, 5, 3, 4, 8], [1, 9, 8, 3, 4, 2, 5, 6, 7], [8, 5, 9, 7, 6, 1, 4, 2, 3], [4, 2, 6, 8, 5, 3, 7, 9, 1], [7, 1, 3, 9, 2, 4, 8, 5, 6], [9, 6, 1, 5, 3, 7, 2, 8, 4], [2, 8, 7, 4, 1, 9, 6, 3, 5], [3, 4, 5, 2, 8, 6, 1, 7, 9]]
[[5, 3, 4, 6, 7, 8, 9, 1, 2], [6, 7, 2, 1, 9, 0, 3, 4, 9], [1, 0, 0, 3, 4, 2, 5, 6, 0], [8, 5, 9, 7, 6, 1, 0, 2, 0], [4, 2, 6, 8, 5, 3, 7, 9, 1], [7, 1, 3, 9, 2, 4, 8, 5, 6], [9, 0, 1, 5, 3, 7, 2, 1, 4], [2, 8, 7, 4, 1, 9, 6, 3, 5], [3, 0, 0, 4, 8, 1, 1, 7, 9]]
[[1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 3, 4, 5, 6, 7, 8, 9, 1], [3, 4, 5, 6, 7, 8, 9, 1, 2], [4, 5, 6, 7, 8, 9, 1, 2, 3], [5, 6, 7, 8, 9, 1, 2, 3, 4], [6, 7, 8, 9, 1, 2, 3, 4, 5], [7, 8, 9, 1, 2, 3, 4, 5, 6], [8, 9, 1, 2, 3, 4, 5, 6, 7], [9, 1, 2, 3, 4, 5, 6, 7, 8]]

import numpy as np

def validSolution(board):
    matrix = np.array(board)
    
    x = check_matrix(matrix)
    y = check_matrix(matrix.transpose())
    z = check_submatrix(matrix)
            
    return x and y and z
    
def check_matrix(m):
    x = True
    for row in m:
        if len(set(row)) == len(m[0]):
            pass
        else:
            x = False
    return x
    
def check_submatrix(m):
    x = True
    
    for i in range(3):
        for j in range(3):
            x = len(np.unique(m[i*3:i*3+3, j*3:j*3+3])) == 9
            
            if not x:
                break
    return x
