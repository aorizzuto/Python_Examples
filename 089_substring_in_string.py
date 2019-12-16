# Write a Python program to find the longest common sub-string from two given strings

from difflib import SequenceMatcher 

def buscar_substring_en_comun(s1,s2):
    seq = SequenceMatcher(None,s1,s2)
    comun = seq.find_longest_match(0, len(s1), 0, len(s2))   # Entrega una estructura con la información del substring en común
    inicio = comun.a                 # a: inicio del string en común
    longitud = comun.size            # size: largo del string en común
    final = inicio + longitud
    return s1[inicio:final] 

#---------------

s1 = ("Alejandro").lower()
s2 = ("Lejos").lower()
x = buscar_substring_en_comun(s1,s2)
print("El string en comun entre \"{}\" y \"{}\" es:\t\t{}".format(s1,s2,x))

s1 = ("Estacionamiento").lower()
s2 = ("Accionar").lower()
x = buscar_substring_en_comun(s1,s2)
print("El string en comun entre \"{}\" y \"{}\" es:\t{}".format(s1,s2,x))

s1 = ("Guitarra").lower()
s2 = ("Jarra").lower()
x = buscar_substring_en_comun(s1,s2)
print("El string en comun entre \"{}\" y \"{}\" es:\t\t{}".format(s1,s2,x))

"""
El string en comun entre "alejandro" y "lejos" es:		lej
El string en comun entre "estacionamiento" y "accionar" es:	ciona
El string en comun entre "guitarra" y "jarra" es:		arra
"""
