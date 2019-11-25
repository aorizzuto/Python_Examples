# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers

seq=input("Ingrese numeros separados por coma: ")

lista=seq.split(',')
tupla=tuple(lista)

print(lista,tupla)

"""
Ingrese numeros separados por coma:  3,1,5,2,4,7,6

['3', '1', '5', '2', '4', '7', '6'] ('3', '1', '5', '2', '4', '7', '6')
"""
