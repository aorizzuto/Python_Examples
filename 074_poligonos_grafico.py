# Write a Python program to check if a point (x,y) is in a triangle or not. There is a triangle formed by three points
# CON GRAFICO!!!

import math
import matplotlib.pyplot as plt
import numpy as np


# -------------------------------------------------------------------
# Calculo b de la ecuación de la recta 

def calc_b(p,x,y):    
        return (p[1] - (y/x)*p[0])   # Despeje Y de la ecuación de la recta tomando 1 punto de la recta para calcular b

# -------------------------------------------------------------------
# Calculo los valores de X y de Y entre dos puntos dados

def calculo_x_y(p_1,p_2):
    x=float(p_1[0])-float(p_2[0])   # Distancia entre puntos x0 y x1
    y=float(p_1[1])-float(p_2[1])   # Distancia entre puntos y0 y y1
    
    if x == 0: # En caso tenga que dibujar una linea vertical
        b = 0                               # No se cruza con el eje Y
        y2 = np.linspace(p_1[1],p_2[1],100) # Genero un vector con 100 puntos desde y0 a y1
        x2 = [p_1[0]]*len(y2)               # Genero un vector con mismas posiciones siempre con valor x
    else:
        b = calc_b(p_1,x,y)                 # Calculo b 
        x2 = np.linspace(p_1[0],p_2[0],100) # 100 Puntos entre x0 y x1
        y2 = (y/x)*x2 + b                   # Ecuacion de la recta
   
    return x2,y2    # Retorno los vectores

# -------------------------------------------------------------------

def grafico_puntos(lst):
    puntos=[]
    for i in lst:
        x = math.cos(i*2*math.pi/360)    # Calculo x e y de acuerdo a los angulos adquiridos en la lista lst
        y = math.sin(i*2*math.pi/360)
        plt.plot(x,y,'bx')               # Dibujo los puntos de los vertices
        puntos.append(round(x,2))        # Guardo puntos en vector
        puntos.append(round(y,2))

    ### Detalles del gráfico ###
    plt.title('Poligono')                # Nombre del grafico
    
    plt.axis([-1.1, 1.1, -1.1, 1.1], 'equal')
    plt.grid(False)                      # Habilito la grilla
    plt.gca().set_aspect("equal")
    plt.axis('on')
    plt.show()                           # Habilito para mostrar el grafico

    return puntos

# -------------------------------------------------------------------

def grafico_lineas(puntos):
    i=0

    for i in range(0,len(puntos)-2,2):
        x,y = calculo_x_y(                  # Obtengo los vectores para dibujar la linea
            [puntos[i+0],puntos[i+1]],
            [puntos[i+2],puntos[i+3]])
        plt.plot(x, y)                      # Dibujo la linea

    x,y = calculo_x_y(
        [puntos[len(puntos)-2],puntos[len(puntos)-1]],
        [puntos[0],puntos[1]])
    plt.plot(x, y)                          # Dibujo la última linea
        
    plt.show()                              # Habilito para mostrar el grafico

# -------------------------------------------------------------------

def calculo_area(lst,ptos,num):
    radio = math.cos(lst[len(lst)-1]*2*math.pi/360)  # Calculo el radio
    
    cateto_x = ptos[0] - ptos[2]                     # Tomo los catetos para calcular uno de los lados
    cateto_y = ptos[1] - ptos[3]
    
    lado = math.sqrt(cateto_x**2 + cateto_y**2)      # Por pitagoras
    
    altura = math.sqrt(radio**2 - (lado/2)**2)       # Altura de cada uno de los triangulos dentro del poligono
    
    return lado * num * altura / 2                   # Retorno el area
    

# -------------------------------------------------------------------
### MAIN ###

s = int(input("Ingrese la cantidad de lados del poligono:"))

lst=[]
ang=0
for i in range(s):    # Creo un vector con los angulos (360/cantidad de lados)
    ang=ang+360/s
    lst.append(ang)

puntos = grafico_puntos(lst)     # Grafico puntos

grafico_lineas(puntos)           # Grafico lineas

a = calculo_area(lst,puntos,s)   # Calculo el area

print("El área es:",a)

