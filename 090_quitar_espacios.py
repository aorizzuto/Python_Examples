# Write a Python program to move all spaces to the front of a given string in single traversal

def contar_espacios(s):
    return s.count(' ') 

#---------------

def quitar_espacios(s):
    return s.replace(' ',"")

s = "A esta sentencia hay que quitarle los espacios y ponerlos al frente"

print(s)

num_espacios = contar_espacios(s)
s = quitar_espacios(s)
espacios = ''.join([" "]*num_espacios)

final_string = espacios+s

print(final_string)

"""
A esta sentencia hay que quitarle los espacios y ponerlos al frente
           Aestasentenciahayquequitarlelosespaciosyponerlosalfrente
"""
