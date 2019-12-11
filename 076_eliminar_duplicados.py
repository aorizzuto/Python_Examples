# Eliminar repetidos

s = input("Ingresar una lista, se eliminaran los duplicados (Ej: 1 3 5 2 4)")

lst = s.split()

lst_s_rep = list(set(lst))

lst_s_rep.sort()

print(lst_s_rep)

"""
Ingresar una lista, se eliminaran los duplicados (Ej: 1 3 5 2 4) 1 3 2 3 4 2 8
['1', '2', '3', '4', '8']
"""
