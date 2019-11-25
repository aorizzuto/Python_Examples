# Escribir un programa que pida al usuario dos números enteros y muestre "<n> entre <m> da un cociente <c> y un resto <r>"
n1=input("Ingrese numero 1:")
n2=input("Ingrese numero 2:")

numero1=float(n1)
numero2=float(n2)

print("{} entre {} da un cociente {} y resto {}".format(numero1,numero2,numero1//numero2,numero1%numero2))

"""
Ingrese numero 1: 18
Ingrese numero 2: 5
18.0 entre 5.0 da un cociente 3.0 y resto 3.0
"""
