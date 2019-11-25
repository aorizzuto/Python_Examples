# Write a Python program which accepts the radius of a circle from the user and compute the area

radio = float(input("Ingrese radio: "))
pi = 3.1415926

print("El area del circulo es: ", pi*(radio**2))
Ingrese radio:  3

"""
El area del circulo es:  28.2743334
"""



#####
# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them

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
