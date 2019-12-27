# Contar cantidad de 1 en matrix
import numpy as np

def count_ones(m):
    y = np.array(m)
    return np.count_nonzero(y == 1)

matrix = [[1,2,3],[4,5,6],[7,8,1],[9,1,1]]
print(count_ones(matrix))

"""
4
"""
