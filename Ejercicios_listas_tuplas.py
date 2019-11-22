# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

num=int(input("Ingrese cantidad de asignaturas:"))
lista=[]

for i in range(num):
    asig=input("Asignatura {}".format(i+1))
    lista.append(asig)

print(lista)

"""
Ingrese cantidad de asignaturas: 3
Asignatura 1 matematica
Asignatura 2 fisica
Asignatura 3 historia
['matematica', 'fisica', 'historia']
"""

# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario
# Conviene usar diccionario

num=int(input("Ingrese cantidad de asignaturas:"))
dicc={}

for i in range(num):
    asig=input("Asignatura {}".format(i+1))
    nota=input("     Nota de {}:".format(asig))
    dicc[asig]=nota

print(dicc)

"""
Ingrese cantidad de asignaturas: 3
Asignatura 1 historia
     Nota de historia: 7
Asignatura 2 matematica
     Nota de matematica: 5
Asignatura 3 fisica
     Nota de fisica: 10
{'historia': '7', 'matematica': '5', 'fisica': '10'}
"""

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



# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

num=int(input("Ingrese cantidad de asignaturas:"))
nota_aprobacion=int(input("Ingrese con que nota se aprueba:"))
dicc={}

for i in range(num):
    asig=input("Asignatura {}".format(i+1))
    nota=int(input("     Nota de {}:".format(asig)))
    
    if nota < nota_aprobacion:
        dicc[asig]=nota
        
print(dicc)

"""
Ingrese cantidad de asignaturas: 3
Ingrese con que nota se aprueba: 4
Asignatura 1 Matematica
     Nota de Matematica: 2
Asignatura 2 Fisica
     Nota de Fisica: 6
Asignatura 3 Quimica
     Nota de Quimica: 5
{'Matematica': 2}
"""

# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in range(len(abc),1,-1):
    if (i%3) == 0:
        abc.pop(i-1)
        
print(abc)

#['a', 'b', 'd', 'e', 'g', 'h', 'j', 'k', 'm', 'n', 'p', 'q', 's', 't', 'v', 'w', 'y', 'z']


# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo

palabra=(input("Escriba una palabra:")).upper()
size=len(palabra)

flag=1

for i in range(size//2):
    if palabra[i] != palabra[size-i-1]:
        flag=0
        break

if flag:
    print(f"{palabra} es un palindromo")
else:
    print(f"{palabra} no es un palindromo")

"""
Escriba una palabra: Sebastianaitsabes
SEBASTIANAITSABES es un palindromo
"""


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


