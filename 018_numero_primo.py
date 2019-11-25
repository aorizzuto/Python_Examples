# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
num=int(input("Ingrese numero entero:"))

ret=1

if num%2 == 1:
    ret = 0
    for i in range(2,num):
        #print("{} {}".format(num,i))
        if num%i == 0:
            ret=1
            break

if ret == 1:
    print("No es primo")
else:
    print("Es primo")

"""
Ingrese numero entero: 23
Es primo
"""
