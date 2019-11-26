# Escribir un programa que almacene dos vectores en dos listas y muestre por pantalla su producto escalar.

vector1=[1,2,3,6]
vector2=[-1,0,2,-3]

def producto_escalar(v1,v2):
    if len(v1) != len(v2):
        return 0
    
    prod = 0
    
    for i in range(len(v1)):
        prod=prod+v1[i]*v2[i]
    
    return prod

print("El producto escalar de {} y {} es: {}".format(vector1,vector2,producto_escalar(vector1,vector2)))

"""
El producto escalar de [1, 2, 3, 6] y [-1, 0, 2, -3] es: -13
"""
