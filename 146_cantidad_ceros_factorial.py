
# Contar la cantidad de ceros en el final del factorial

def zeros(n):
    i = 5
    z = 0
    while n >= i:
        z += n // i
        i *= 5
    return z
