# Ordenar y eliminar duplicados de una lista

def ejercicio(lista):
    lista_sin_repetidos = list(set(lista))
    lista_sin_repetidos.sort()
    return lista_sin_repetidos

lista=[1, 3, 4, 5, 6, 100, 27]

lista_final = ejercicio(lista)

print(lista_final)
