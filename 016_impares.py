# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
import math

lista=[]
num=int(input("Ingrese numero entero:"))

for i in range(math.ceil(num/2)):
    lista.append(i*2+1)

print(','.join(str(e) for e in lista))

"""
Ingrese numero entero: 24
1,3,5,7,9,11,13,15,17,19,21,23
"""
