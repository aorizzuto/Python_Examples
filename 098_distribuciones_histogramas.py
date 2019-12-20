import random
import numpy as np
import matplotlib.pyplot as plt

datos=10000

mu = 100 # Media de la distribución
sigma = 15 # desviacion estandar
x = mu + sigma * np.random.randn(datos)

x = [random.uniform(0,3) for i in range(0,datos)]


### UNIFORM ### 

g = plt.figure(1)

plt.title('Histograma')
plt.xlabel('Datos')

n, bins, patches = plt.hist(x, bins='auto')
g.show()

"""
    # UNIFORM
print("\nUniform(min:1.2,max:2.5):",random.uniform(1.2,2.5))

    # TRIANGULAR
print("\nTriangular(low:1,high:2,mas cerca de:1):",random.triangular(1,2,1))

    # DISTRIBUCION BETA
print("\nDistribución Beta - betavariate(2,5):",random.betavariate(2,5))

    # DISTRIBUCION EXPONENCIAL
print("\nDistribución Exponencial - expovariate(2):",random.expovariate(2))

    # DISTRIBUCION GAMMA
print("\nDistribución Gamma - gammavariate(alpha:1,beta:3):",random.gammavariate(1,3))

    # DISTRIBUCION GAUSS
print("\nDistribución Gamma - gauss(mu:1,sigma:3):",random.gauss(1,3))

    # DISTRIBUCION LOG
print("\nDistribución Log - gauss(mu:1,sigma:3):",random.lognormvariate(1, 3))

    # DISTRIBUCION NORMAL
print("\nDistribución Normal - gauss(mu:1,sigma:3):",random.normalvariate(1, 3))

    # DISTRIBUCION 
print("\nDistribución Vonmises - gauss(mu:1,kappa:3):",random.vonmisesvariate(1, 3))

    # DISTRIBUCION PARETO
print("\nDistribución Pareto - gauss(alpha:1):",random.paretovariate(1))

    # DISTRIBUCION WEIBULL
print("\nDistribución Weibull - gauss(alpha:1,beta:3):",random.weibullvariate(1, 3))
"""
