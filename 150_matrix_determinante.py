
# Determinante de una matriz

import numpy as np

def determinant(matrix):
    a = np.array(matrix)
    return round(np.linalg.det(a))
