# Write a Python program to test whether two lines PQ and RS are parallel. The four points are P(x1, y1), Q(x2, y2), R(x3, y3), S(x4, y4)

def paralelas(s):
    lst = list(map(int,s.split()))

    p1 = (lst[3]-lst[1])/(lst[2]-lst[0])
    p2 = (lst[7]-lst[5])/(lst[6]-lst[4])

    if p1 == p2:
        return 1
    else:
        return 0

s = input("Inserte los 4 puntos de las 2 rectas separados por espacio (x1 y1 x2 y2 x3 y3 x4 y4):")
par = paralelas(s)

if par:
    print("Son paralelas")
else:
    print("No son paralelas")
    
"""
Inserte los 4 puntos de las 2 rectas separados por espacio (x1 y1 x2 y2 x3 y3 x4 y4): 1 2 3 6 4 8 5 10
Son paralelas
"""
