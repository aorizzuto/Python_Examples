# Write a Python program to calculate number of days between two dates

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
