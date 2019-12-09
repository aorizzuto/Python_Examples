# Write a Python program to compute the sum of first n given prime numbers

def primo (num):
    ret=1
    if num%2 == 0:
        ret = 0
    else:
        for i in range(2,num):
            if num%i == 0:
                ret=0
                break
    return ret

### MAIN ###
numero = int(input("Ingrese numero para entregar la suma de los numeros primos menores a este:"))

lista=[]
lista.append(1)
lista.append(2)
for i in range(3,numero+1):
    if primo(i):
        lista.append(i)

print("Los numeros primos menores a {} son {}".format(numero,lista))
print("La suma de estos es:",sum(lista))

"""
Ingrese numero para entregar la suma de los numeros primos menores a este: 23
Los numeros primos menores a 23 son [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]
La suma de estos es: 101
"""
