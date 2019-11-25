# Escribir un programa que pregunte el nombre del usuario y luego muestre por pantalla <NOMBRE> tiene <n> letras, 
# donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.

nombre=input("Introduzca el nombre:")
print(f"{nombre.upper()} tiene {len(nombre)} letras")

"""
Introduzca el nombre: Alejandro
ALEJANDRO tiene 9 letras
"""
