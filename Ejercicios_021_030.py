# 1) Write a Python program which accepts the radius of a circle from the user and compute the area

radio = float(input("Ingrese radio: "))
pi = 3.1415926

print("El area del circulo es: ", pi*(radio**2))
Ingrese radio:  3

"""
El area del circulo es:  28.2743334
"""



#####
# 2) Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them

####### Función Inversa #########

def inversa(nombre,apellido):
    completo = nombre + " " + apellido
    size = len(completo)

    inversa = ""
    for i in range(size):
        inversa = inversa + completo[size-i-1]
        
    return inversa

#################################

nombre = input("Nombre: ")
apellido = input("Apellido: ")

inv = inversa(nombre, apellido)

print(inv)

"""
Nombre:  Alejandro
Apellido:  Fernandez
zednanreF ordnajelA
"""




# 3) Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers

seq=input("Ingrese numeros separados por coma: ")

lista=seq.split(',')
tupla=tuple(lista)

print(lista,tupla)
Ingrese numeros separados por coma:  3,1,5,2,4,7,6

"""
['3', '1', '5', '2', '4', '7', '6'] ('3', '1', '5', '2', '4', '7', '6')
"""


# 4) Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn

n=input("Ingrese numero. Se entregará el valor n+nn+nnn: ")

nn=n+n
nnn=n+nn


print(int(nnn)+int(nn)+int(n))

"""
Ingrese numero. Se entregará el valor n+nn+nnn:  6
738
"""



