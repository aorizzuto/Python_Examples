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
