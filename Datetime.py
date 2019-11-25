# Write a Python program to get the Python version you are using

import sys

print(sys.version)
print(sys.version_info)

"""
3.7.3 | packaged by conda-forge | (default, Jul  1 2019, 21:52:21) 
[GCC 7.3.0]
sys.version_info(major=3, minor=7, micro=3, releaselevel='final', serial=0)
""2


# Write a Python program to display the current date and time.

from datetime import date, datetime, time

hoy = date.today()
time = datetime.now()

print("Dia:\t\t", hoy.day)
print("Mes:\t\t", hoy.month)
print("Año:\t\t", hoy.year)

print("Horas:  \t", time.strftime("%H")) 
print("Minutos: \t", time.strftime("%M")) 
print("Segundos: \t", time.strftime("%S"))

"""
Dia:		 25
Mes:		 11
Año:		 2019
Horas:  	 10
Minutos: 	 39
Segundos: 	 30
"""
