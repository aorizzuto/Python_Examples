# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

lista=[]

while True:
    num=int(input("Ingrese numeros aleatoriamente (0 para salir):"))
    if num == 0:
        break;
    lista.append(num)  

if len(lista) > 0:
    lista.sort()
    
    print("Lista ordenada:")
    print(lista)

"""
Ingrese numeros aleatoriamente (0 para salir): 6
Ingrese numeros aleatoriamente (0 para salir): 18
Ingrese numeros aleatoriamente (0 para salir): 4
Ingrese numeros aleatoriamente (0 para salir): 21
Ingrese numeros aleatoriamente (0 para salir): 50
Ingrese numeros aleatoriamente (0 para salir): 23
Ingrese numeros aleatoriamente (0 para salir): 15
Ingrese numeros aleatoriamente (0 para salir): 70
Ingrese numeros aleatoriamente (0 para salir): 0
Lista ordenada:
[4, 6, 15, 18, 21, 23, 50, 70]
"""
