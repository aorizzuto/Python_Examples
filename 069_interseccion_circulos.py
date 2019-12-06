# There are two circles C1 with radius r1, central coordinate (x1, y1) and C2 with radius r2 and central coordinate (x2, y2)


import math
import matplotlib.pyplot as plt
import numpy as np

   
def grafico(lst):
    p1=[float(lst[0]),float(lst[1]),float(lst[2])]   # x0,y0
    p2=[float(lst[3]),float(lst[4]),float(lst[5])]   # x1,y1

    x,y = calculo_x_y(p1)
    plt.plot(x, y, label='Circulo 1')              # Dibujo la anterior linea
    
    x,y = calculo_x_y(p2)
    plt.plot(x, y, label='Circulo 2')              # Dibujo la anterior linea

    ### Detalles del gráfico ###
    plt.title('Ejercicio Lineas Paralelas')  # Nombre del grafico
    plt.xlabel('x')         # Nombre del eje X
    plt.ylabel('y')         # Nombre del eje Y
    plt.legend()            # Muestra los label
    plt.grid()              # Habilito la grilla
    plt.xlim([0,10])         # Limites del eje X
    plt.ylim([0,10])         # Limites del eje Y
    plt.show()              # Habilito para mostrar el grafico




    



def calculo_x_y(p):
    th = np.linspace(0,2*np.pi,100)   # 100 Puntos entre x0 y x1
    radio = p[2]
 
    x = radio*np.cos(th)+p[0]
    y = radio*np.sin(th)+p[1]
    
    return x,y
    


### MAIN ###
    
s = input("Inserte los 3 puntos de las 2 circunferencias separados por espacio (x1 y1 r1 x2 y2 r2):")
lst = list(map(int,s.split()))

grafico(lst)

hip = math.sqrt((lst[3]-lst[0])**2 + (lst[4]-lst[1])**2)

print(hip,lst[2],lst[5])

if hip < lst[2]-lst[5]:
    print("C2  dentro de C1")
elif hip < lst[5]-lst[2]:
    print("C1  dentro de C2")
elif hip > lst[2]+lst[5]:
    print("No hay intersección entre las circunferencias")
else:
    print("Hay intersección")
    

# Prueba intersección: 2 3 2 6 5 3
# Prueba sin interseccion: 2 3 2 6 5 2
# Prueba C2 dentro de C1: 5 5 5 4 4 1
# Prueba C1 dentro de C2: 4 4 1 5 5 5
