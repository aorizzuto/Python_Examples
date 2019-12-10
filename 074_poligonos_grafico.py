# Write a Python program to check if a point (x,y) is in a triangle or not. There is a triangle formed by three points
# CON GRAFICO!!!

import math
import matplotlib.pyplot as plt
import numpy as np




### Calculo b de la ecuación de la recta ###

def calc_b(p,x,y):
        return (p[1] - (y/x)*p[0])





### Calculo los valores de X y de Y entre dos puntos dados ###

def calculo_x_y(p_1,p_2):
    x=float(p_1[0])-float(p_2[0])   # Distancia entre puntos x0 y x1
    y=float(p_1[1])-float(p_2[1])   # Distancia entre puntos y0 y y1
    
    if x == 0:
        b = 0
        y2 = np.linspace(p_1[1],p_2[1],100)
        x2 = [p_1[0]]*len(y2)
    else:
        b = calc_b(p_1,x,y)
        x2 = np.linspace(p_1[0],p_2[0],100)   # 100 Puntos entre x0 y x1
        y2 = (y/x)*x2 + b                     # Ecuacion de la recta
   
    return x2,y2









def grafico_puntos(lst):
    puntos=[]
    for i in lst:
        x = math.cos(i*2*math.pi/360)
        y = math.sin(i*2*math.pi/360)
        plt.plot(x,y,'bx')
        puntos.append(round(x,2))
        puntos.append(round(y,2))

    ### Detalles del gráfico ###
    plt.title('Poligono')  # Nombre del grafico
    
    plt.axis([-1.1, 1.1, -1.1, 1.1], 'equal')
    plt.grid(False)              # Habilito la grilla
    plt.gca().set_aspect("equal")
    plt.axis('on')
    plt.show()              # Habilito para mostrar el grafico

    return puntos



def grafico_lineas(puntos):
    i=0
    print(puntos)
    for i in range(0,len(puntos)-2,2):
        x,y = calculo_x_y(
            [puntos[i+0],puntos[i+1]],
            [puntos[i+2],puntos[i+3]])
        plt.plot(x, y)              # Dibujo la linea

    x,y = calculo_x_y(
        [puntos[len(puntos)-2],puntos[len(puntos)-1]],
        [puntos[0],puntos[1]])
    plt.plot(x, y)              # Dibujo la última linea
        
    ### Detalles del gráfico ###
    plt.show()              # Habilito para mostrar el grafico



    
### MAIN ###

s = int(input("Inserte la cantidad de lados del poligono:"))

lst=[]
ang=0
for i in range(s):
    ang=ang+360/s
    lst.append(ang)

puntos = grafico_puntos(lst)

grafico_lineas(puntos)


