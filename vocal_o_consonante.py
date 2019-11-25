# Write a Python program to test whether a passed letter is a vowel or not

print("\n¿ES VOCAL?\n")

while True:
    l=input("Introduzca una letra:")
    letra=(l).upper()

    tupla=("A","E","I","O","U")

    if letra in tupla:
        print(f"La letra {letra} es una vocal")
    else:
        print(f"La letra {letra} es una consonante")    

"""
¿ES VOCAL?

Introduzca una letra: a
La letra A es una vocal
Introduzca una letra: m
La letra M es una consonante
Introduzca una letra: o
La letra O es una vocal
Introduzca una letra: y
La letra Y es una consonante
"""
