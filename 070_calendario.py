# Write a Python program to that reads a date (from 2016/1/1 to 2016/12/31) and prints the day of the date. Jan. 1, 2016, is Friday. 
# Note that 2016 is a leap year

import calendar

s = input("Ingrese mes y dia separados por espacio (mm dd):")
anio=2016

date = list(map(int,s.split()))
c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(anio, date[0])
print(str)

day = calendar.weekday(anio,date[0],date[1])

print(calendar.day_name[day-1])

"""
Ingrese mes y dia separados por espacio (mm dd): 03 04
     March 2016
Su Mo Tu We Th Fr Sa
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31

Thursday
"""
