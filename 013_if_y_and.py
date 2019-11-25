# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
edad=int(input("Ingrese edad:"))
ingresos=float(input("Ingrese ingresos (euros):"))

ingresos_max=1000
edad_max=16

if edad > edad_max and ingresos >= ingresos_max:
    print("Puede tributar")
else:
    print("No puede tributar")

"""
Ingrese edad: 33
Ingrese ingresos (euros): 999
No puede tributar

Ingrese edad: 17
Ingrese ingresos (euros): 1000
Puede tributar
"""
