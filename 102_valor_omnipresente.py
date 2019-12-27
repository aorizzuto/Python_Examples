# Verificar si "val" se encuentra en toda la lista

def is_omnipresent(lst, val):
    return all([val in i for i in lst])

l=[[1,2,3,4,5,6],[1,2,3],[4,5,6,3],[3,1]]
n=3
print(l)
print("Se buscará el valor:",n)
print(is_omnipresent(l,n))

"""
[[1, 2, 3, 4, 5, 6], [1, 2, 3], [4, 5, 6, 3], [3, 1]]
Se buscará el valor: 3
True
"""
