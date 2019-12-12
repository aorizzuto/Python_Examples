# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo

palabra=(input("Escriba una palabra:")).upper()
size=len(palabra)

flag=1

for i in range(size//2):
    if palabra[i] != palabra[size-i-1]:
        flag=0
        break

if flag:
    print(f"{palabra} es un palindromo")
else:
    print(f"{palabra} no es un palindromo")

"""
Escriba una palabra: Sebastianaitsabes
SEBASTIANAITSABES es un palindromo
"""


######## OTRA FORMA ##########

def es_palindromo(txt):
	return txt == txt[::-1]
