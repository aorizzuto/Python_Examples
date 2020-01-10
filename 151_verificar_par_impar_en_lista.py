# Verificar cual es el numero que es par o impar en la lista

def iq_test(numbers):
    num = [int(i)%2 for i in numbers.split()]
    if num.count(1) == 1:
        return num.index(1)+1
    else:
        return num.index(0)+1
