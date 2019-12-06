# There are two circles C1 with radius r1, central coordinate (x1, y1) and C2 with radius r2 and central coordinate (x2, y2)
# 2 3 2 6 5 3

import math
import matplotlib.pyplot as plt
import numpy as np

   
def grafico(lst):
    p1=[float(lst[0]),float(lst[1])]   # x0,y0
    p2=[float(lst[2]),float(lst[3])]   # x1,y1
    p3=[float(lst[4]),float(lst[5])]   # x2,y2
    p4=[float(lst[6]),float(lst[7])]   # x4,y4

    x,y = calculo_x_y(p1,p2)
    plt.plot(x, y, label='Linea 1')              # Dibujo la anterior linea
    x,y = calculo_x_y(p3,p4)
    plt.plot(x, y, label='Linea 2')              # Dibujo la anterior linea

    ### Detalles del gráfico ###
    plt.title('Ejercicio Lineas Paralelas')  # Nombre del grafico
    plt.xlabel('x')         # Nombre del eje X
    plt.ylabel('y')         # Nombre del eje Y
    plt.legend()            # Muestra los label
    plt.grid()              # Habilito la grilla
    plt.xlim([0,10])         # Limites del eje X
    plt.ylim([0,10])         # Limites del eje Y
    plt.show()              # Habilito para mostrar el grafico

    

    
### Calculo b de la ecuación de la recta ###

def calc_b(p,x,y):
    return (p[1] - (y/x)*p[0])





### Calculo los valores de X y de Y entre dos puntos dados ###

def calculo_x_y(p_1,p_2):
    x=float(p_1[0])-float(p_2[0])   # Distancia entre puntos x0 y x1
    y=float(p_1[1])-float(p_2[1])   # Distancia entre puntos y0 y y1

    b = calc_b(p_1,x,y)
    x2 = np.linspace(p_1[0],p_2[0],100)   # 100 Puntos entre x0 y x1
    y2 = (y/x)*x2 + b                     # Ecuacion de la recta
    
    return x2,y2




### MAIN ###
    
s = input("Inserte los 4 puntos de las 2 rectas separados por espacio (x1 y1 r1 x2 y2 r2):")
lst = list(map(int,s.split()))

grafico(lst)

