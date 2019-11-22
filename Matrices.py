# Función para crear matrices indicando filas(f), columnas(c) y valor(n). Luego de creación se debe llenar la matriz con los valores correctos
def new_matriz(f,c,n):
    matriz = []
    for i in range(f):
        a = [n]*c
        matriz.append(a)
    return matriz

m1=new_matriz(3,4,0)

print(m1)

# Output: [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
