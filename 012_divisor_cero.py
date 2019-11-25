# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
# Si el divisor es cero el programa debe mostrar un error.
# Este ejercicio también puede realizarse con try-exception

numero1=float(input("Ingrese numero 1:"))
numero2=float(input("Ingrese numero 2:"))

if numero2 == 0:
    print("Error: divisor igual a 0")
else:
    print("Division: {}".format(numero1/numero2))

"""
Ingrese numero 1: 5
Ingrese numero 2: 0
Error: divisor igual a 0

Ingrese numero 1: 10
Ingrese numero 2: 3
Division: 3.3333333333333335
"""
