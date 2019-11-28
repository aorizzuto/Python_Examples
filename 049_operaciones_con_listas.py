print("Lista de letras y numeros")

lst=[1,5,2,"a",6,"l","j",9,"b",0,3]

print(lst)

print("\nElimino las letras:")
lst_int=[x for x in lst if isinstance(x,int)]
print(lst_int)

print("\nBorro la lista:")
new_lst.clear()
print(new_lst)

print("\nElimino los numeros:")
lst_str=[x for x in lst if isinstance(x,str)]
print(lst_str)

print("\nInvierto la lista:")
new_lst=lst
new_lst.reverse()
print(new_lst)

print("\nOrdeno la lista:")
lst_int.sort()
lst_str.sort()
new_lst = lst_int + lst_str
print(new_lst)
new_lst = lst_str + lst_int
print(new_lst)

print("\nElimino 3er elemento:")
lst.reverse()
del lst[2]
print(lst)

"""
Lista de letras y numeros
[1, 5, 2, 'a', 6, 'l', 'j', 9, 'b', 0, 3]

Elimino las letras:
[1, 5, 2, 6, 9, 0, 3]

Borro la lista:
[]

Elimino los numeros:
['a', 'l', 'j', 'b']

Invierto la lista:
[3, 0, 'b', 9, 'j', 'l', 6, 'a', 2, 5, 1]

Ordeno la lista:
[0, 1, 2, 3, 5, 6, 9, 'a', 'b', 'j', 'l']
['a', 'b', 'j', 'l', 0, 1, 2, 3, 5, 6, 9]

Elimino 3er elemento:
[1, 5, 'a', 6, 'l', 'j', 9, 'b', 0, 3]
"""
