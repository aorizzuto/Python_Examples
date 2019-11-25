# 4) Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn

n=input("Ingrese numero. Se entregará el valor n+nn+nnn: ")

nn=n+n
nnn=n+nn

print(int(nnn)+int(nn)+int(n))

"""
Ingrese numero. Se entregará el valor n+nn+nnn:  6
738
"""
