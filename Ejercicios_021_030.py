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


# 5) Write a Python program to print the calendar of a given month and year.

print("CALENDARIO\n")

import calendar

anio=int(input("Ingrese el año:"))
mes=int(input("Ingrese el número del mes (1-12):"))
cal = calendar.TextCalendar(calendar.SUNDAY) # Donde va a empezar la semana

str = cal.formatmonth(anio,mes)
print("\n",str)

"""
CALENDARIO

Ingrese el año: 2020
Ingrese el número del mes (1-12): 4

      April 2020
Su Mo Tu We Th Fr Sa
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30
"""







# 6) Write a Python program to calculate number of days between two dates

from datetime import datetime

print("\nDIFERENCIA ENTRE FECHAS\n")

fecha1=input("Ingrese la fecha MENOR separada por espacios(Ej: DD MM YYYY):")
fecha2=input("Ingrese la fecha MAYOR separada por espacios(Ej: DD MM YYYY):")

date1 = datetime.strptime(fecha1, '%d %m %Y')
date2 = datetime.strptime(fecha2, '%d %m %Y')

print("{} dias de diferencia".format(abs((date2-date1).days)))

"""
DIFERENCIA ENTRE FECHAS

Ingrese la fecha MENOR separada por espacios(Ej: DD MM YYYY): 03 03 1991
Ingrese la fecha MAYOR separada por espacios(Ej: DD MM YYYY): 25 11 2019
10494 dias de diferencia
"""
