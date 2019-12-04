# Write a Python program to check if a point (x,y) is in a triangle or not. There is a triangle formed by three points

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

    b = calc_b(p_1,x,y)
    x2 = np.linspace(p_1[0],p_2[0],100)   # 100 Puntos entre x0 y x1
    y2 = (y/x)*x2 + b                     # Ecuacion de la recta
    
    return x2,y2





def calcular_y(p1,p2,x):
    x12=float(p2[0])-float(p1[0])   
    y12=float(p2[1])-float(p1[1])   
        
    b12 = calc_b(p2,x12,y12)
    return ((y12/x12)*x + b12)    # Ecuacion de la recta







### Verifico si el punto se encuentra dentro del triangulo ###

def verificar_punto(p1,p2,p3,pto):
    x = pto[0]
    y = pto[1]
    
    xs = [p1[0],p2[0],p3[0]]
    xs.sort()
    
    if x < p1[0] or x > p3[0]:
        return 0
    else:
        if x < p2[0]:
            lugar = 1        # El punto esta entre p12 y p13
        else:
            lugar = 2        # El punto esta entre p23 y p13
    
    
    
    
    if lugar == 1:
        
        y_list = [calcular_y(p1,p2,x),calcular_y(p1,p3,x)]
        
    else:
        y_list = [calcular_y(p2,p3,x),calcular_y(p1,p3,x)]
    
    
    y_list.sort()
    
    if y > min(y_list) and y < max(y_list):
        return 1 
    else:
        return 0

    
    
    
    
### MAIN ###

s = input("Inserte 3 puntos (X1 X2 Y1 Y2 Z1 Z2):")
lst = s.split()

s = input("Inserte punto a verificar:")
pto = list(map(int, s.split()))

p1=[float(lst[0]),float(lst[1])]   # x0,y0
p2=[float(lst[2]),float(lst[3])]   # x1,y1
p3=[float(lst[4]),float(lst[5])]   # x2,y2

verificar_punto(p1,p2,p3,pto)







### Grafico ###
x,y = calculo_x_y(p1,p2)
plt.plot(x, y, label='p1-p2')              # Dibujo la anterior linea

x,y = calculo_x_y(p2,p3)
plt.plot(x, y, label='p2-p3')              # Dibujo la anterior linea

x,y = calculo_x_y(p3,p1)
plt.plot(x, y, label='p3-p1')              # Dibujo la anterior linea

plt.plot(pto[0],pto[1],'bx', label='Punto a verificar')

### Detalles del gráfico ###
plt.title('Triangulo')  # Nombre del grafico
plt.xlabel('x')         # Nombre del eje X
plt.ylabel('y')         # Nombre del eje Y
plt.legend()            # Muestra los label
plt.grid()              # Habilito la grilla
plt.xlim([0,5])         # Limites del eje X
plt.ylim([0,5])         # Limites del eje Y
plt.show()              # Habilito para mostrar el grafico

