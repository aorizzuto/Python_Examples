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
