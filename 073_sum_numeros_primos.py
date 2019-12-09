# Write a Python program that accept a even number (>=4, Goldbach number) from the user and create a combinations that express the given number as a sum of two prime numbers. Print the number of combinations

def es_primo (num):
    ret=1
    if num%2 == 0:
        ret = 0
    else:
        for i in range(2,num):
            if num%i == 0:
                ret=0
                break
    return ret

def get_lista_primos(num):
    lista=[]
    for i in range(3,num+1):
        if es_primo(i):
            lista.append(i)
    return lista

### MAIN ###
numero = int(input("Ingrese numero para entregar la combinacion de 2 numeros primos que sumados del este numero:"))

lista = get_lista_primos(numero)
lista.sort()

usados=[]

print(lista)
flag=0
for i in lista:
    for j in lista:
        if i+j == numero:
            flag=1
            if i not in usados:
                print(f"{i} + {j} = {numero}")
                usados.append(i)
                usados.append(j)
            
if not flag:
    print("No hay combinaciones")
    
"""
Ingrese numero para entregar la combinacion de 2 numeros primos que sumados del este numero: 100
[3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
3 + 97 = 100
11 + 89 = 100
17 + 83 = 100
29 + 71 = 100
41 + 59 = 100
47 + 53 = 100
"""
