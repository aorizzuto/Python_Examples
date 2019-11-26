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
