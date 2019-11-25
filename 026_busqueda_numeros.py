# Write a Python program to count a number in a given list

print("\nBUSCAR NUMEROS")

num=input("Ingresar numero a buscar:")
string=input("Ingresar numeros separados por coma (Ej: 1,2,3,4):")

lista=string.split(',')

contador=0
for i in range(len(lista)):
    if lista[i] == num:
        contador+=1

if contador != 0:
    print("El numero {} se repite {} veces".format(num,contador))

"""
BUSCAR NUMEROS
Ingresar numero a buscar: 4
Ingresar numeros separados por coma (Ej: 1,2,3,4): 1,4,2,4,4,7,9,8,4,20,4,6,4,19,4
El numero 4 se repite 7 veces
"""
