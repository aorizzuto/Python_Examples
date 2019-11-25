# Write a Python program to print the calendar of a given month and year.

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
