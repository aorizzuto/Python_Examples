# Ordenar y eliminar duplicados de una lista

def ejercicio(lista):
    lista_sin_repetidos = set(lista)
    sorted(lista_sin_repetidos)
    return lista_sin_repetidos

lista=[1,3,6,6,4,2,2,1,2,4,5]

lista_final = ejercicio(lista)

print(lista_final)
