# Write a Python program to compute the distance between the points (x1, y1) and (x2, y2)

import math
import matplotlib.pyplot as plt
import numpy as np

def get_distancia(x,y):
    return math.sqrt(x**2 + y**2)

punto1=input("Ingrese las coordenadas del primer punto:")
punto2=input("Ingrese las coordenadas del segundo punto:")

p1=list(punto1.split())
p2=list(punto2.split())

x1_i=float(p1[0])
x2_i=float(p2[0])

x=float(p1[0])-float(p2[0])
y=float(p1[1])-float(p2[1])
    
d=get_distancia(x,y)

print("La distancia entre los puntos {} y {} es {}".format(p1,p2,d))

    
### Grafico ###

x2 = np.linspace(x1_i,x2_i,100)
y2 = (y/x)*x2
plt.plot(x2, y2, '-r', label='y')
plt.title('Grafico')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.grid()
plt.xlim([0,5]) # Hay que buscar la minima y maxima X e Y
plt.ylim([0,5])
plt.show()

"""
Ingrese las coordenadas del primer punto: 0.5 1
Ingrese las coordenadas del segundo punto: 4.3 4.7
La distancia entre los puntos ['0.5', '1'] y ['4.3', '4.7'] es 5.303772242470448
"""
