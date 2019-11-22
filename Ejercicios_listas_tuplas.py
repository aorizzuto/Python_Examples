# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

num=int(input("Ingrese cantidad de asignaturas:"))
lista=[]

for i in range(num):
    asig=input("Asignatura {}".format(i+1))
    lista.append(asig)

print(lista)

-----------------------
Ingrese cantidad de asignaturas: 3
Asignatura 1 matematica
Asignatura 2 fisica
Asignatura 3 historia
['matematica', 'fisica', 'historia']
-----------------------

# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario
# Conviene usar diccionario

num=int(input("Ingrese cantidad de asignaturas:"))
dicc={}

for i in range(num):
    asig=input("Asignatura {}".format(i+1))
    nota=input("     Nota de {}:".format(asig))
    dicc[asig]=nota

print(dicc)

-----------------------
Ingrese cantidad de asignaturas: 3
Asignatura 1 historia
     Nota de historia: 7
Asignatura 2 matematica
     Nota de matematica: 5
Asignatura 3 fisica
     Nota de fisica: 10
{'historia': '7', 'matematica': '5', 'fisica': '10'}
-----------------------

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

-----------------------
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
-----------------------




