# Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

lista=[]

while True:
    precio=int(input("Escriba un precio (0 para terminar):"))
    if precio == 0:
        break;

    lista.append(precio)
    
lista.sort()

print("El menor precio es: {}".format(lista[0]))

print("El mayor precio es: {}".format(lista[len(lista)-1]))

"""
Escriba un precio (0 para terminar): 9
Escriba un precio (0 para terminar): 2
Escriba un precio (0 para terminar): 8
Escriba un precio (0 para terminar): 5
Escriba un precio (0 para terminar): 28
Escriba un precio (0 para terminar): 16
Escriba un precio (0 para terminar): 13
Escriba un precio (0 para terminar): 1
Escriba un precio (0 para terminar): 33
Escriba un precio (0 para terminar): 4
Escriba un precio (0 para terminar): 0
El menor precio es: 1
El mayor precio es: 33
"""
