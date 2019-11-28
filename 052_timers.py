# Write a Python program to calculate the time runs (difference between start and current time) of a program

from timeit import default_timer

def timer(n):
    print("Diferencia de tiempos entre inicio y final para {} segundos:".format(n))
    
    start = default_timer()

    for row in range(0,n):
        print(row+1)
        
    print((default_timer() - start)*1000,"ms\n")

timer(5)
timer(15)

"""
Diferencia de tiempos entre inicio y final para 5 segundos:
1
2
3
4
5
0.623480000285781 ms

Diferencia de tiempos entre inicio y final para 15 segundos:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
3.0230020001908997 ms
"""
