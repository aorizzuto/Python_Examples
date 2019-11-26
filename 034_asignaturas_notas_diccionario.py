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
