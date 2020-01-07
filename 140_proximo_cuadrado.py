# Buscar proximo cuadrado si el valor dado por parametro es un cuadrado

import math
def find_next_square(sq):
    return (int(math.sqrt(sq))+1)**2 if (math.sqrt(sq)).is_integer() else -1

