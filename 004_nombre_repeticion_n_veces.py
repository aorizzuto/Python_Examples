# Escribir un programa que pregunte el nombre del usuario y un número entero e imprima, en líneas distintas, el nombre del usuario tantas veces como el número introducido.
nombre=input("Introduzca el nombre: ")
numero=input("Numero de repetición: ")

for i in range(int(numero)):
    print(nombre)

"""
Introduzca el nombre:  Ale
Numero de repetición:  3
Ale
Ale
Ale
"""
