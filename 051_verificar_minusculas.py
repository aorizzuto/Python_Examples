# Write a Python program to check if lowercase letters exist in a string

def verificar_lowercase(string):
    print(f"Vemos si el string tiene caracteres lowercase: \"{string}\"")
    return any(c.islower() for c in string)

string = "ESTE ES EL sTRING"
if verificar_lowercase(string): 
    print("Hay minusculas")
else:
    print("No hay minusculas")

"""
Vemos si el string tiene caracteres lowercase: "ESTE ES EL sTRING"
Hay minusculas
"""
