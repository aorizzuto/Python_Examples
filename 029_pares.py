# Crear función que tome los valores pares desde 1 hasta el número elegido

def find_even_nums(num):
    vals = [i for i in range(1,num+1) if i%2 == 0]
    return vals

num=int(input("Ingresar numero:"))
print(find_even_nums(num))

"""
Ingresar numero:13
[2, 4, 6, 8, 10, 12]
"""
