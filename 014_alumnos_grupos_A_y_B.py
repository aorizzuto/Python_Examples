"""
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y 
el grupo B por elresto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
"""
nombre=input("Ingrese nombre:")
sexo=input("Ingrese sexo (F o M):")

if (nombre[0].upper() > 'N' and sexo == 'M') or (nombre[0].upper() < 'M' and sexo == 'F'):
    print("Grupo A")
else:
    print("Grupo B")

"""
Ingrese nombre: Natalia
Ingrese sexo (F o M): F
Grupo B

Ingrese nombre: Omar
Ingrese sexo (F o M): M
Grupo A

Ingrese nombre: Belen
Ingrese sexo (F o M): F
Grupo A

Ingrese nombre: Claudio
Ingrese sexo (F o M): M
Grupo B
"""
