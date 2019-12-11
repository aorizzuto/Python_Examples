# Contar caracteres

from collections import Counter 
  
s = input("Ingrese una cadena de texto:")
    
res = Counter(s) 
  
print ("\nUsando Counter:\n", res)

res = {} 
  
for keys in s: 
    res[keys] = res.get(keys, 0) + 1

print("\nUsando diccionario:\n", res)

res = {i : s.count(i) for i in set(s)} 

print("\nUsando for:\n", res)

"""
Ingrese una cadena de texto: Alejandro Rizzuto

Usando Counter:
 Counter({'o': 2, 'z': 2, 'A': 1, 'l': 1, 'e': 1, 'j': 1, 'a': 1, 'n': 1, 'd': 1, 'r': 1, ' ': 1, 'R': 1, 'i': 1, 'u': 1, 't': 1})

Usando diccionario:
 {'A': 1, 'l': 1, 'e': 1, 'j': 1, 'a': 1, 'n': 1, 'd': 1, 'r': 1, 'o': 2, ' ': 1, 'R': 1, 'i': 1, 'z': 2, 'u': 1, 't': 1}

Usando for:
 {'A': 1, 'n': 1, 'l': 1, ' ': 1, 'R': 1, 'o': 2, 'a': 1, 't': 1, 'u': 1, 'i': 1, 'e': 1, 'j': 1, 'r': 1, 'd': 1, 'z': 2}
 """
