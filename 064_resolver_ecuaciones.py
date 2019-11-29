# Write a Python program which solve the equation: 
# ax+by=c
# dx+ey=f

import numpy as np

s = input("Ingrese los parametros a,b,c,d,e,f:")
lst = s.split(',')
lst = [int(i) for i in lst] 

fst = lst[:2]
snd = lst[3:5]
trd = [lst[2],lst[5]]

print(fst,snd,trd)

A = np.array([ fst, snd ])
b = np.array(trd)
z = np.linalg.solve(A,b)
print("X = {}\nY = {}".format(z[0],z[1]))

"""
Ingrese los parametros a,b,c,d,e,f: 1,2,3,4,5,6
[1, 2] [4, 5] [3, 6]
X = -1.0
Y = 2.0
"""
