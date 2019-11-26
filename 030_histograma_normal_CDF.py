# Write a Python program to create a histogram from a given list of integers
import numpy as np
import matplotlib.pyplot as plt


# example data
mu = 100 # Media de la distribución
sigma = 15 # desviacion estandar
x = mu + sigma * np.random.randn(100000)

### Primer gráfico ### CDF
f = plt.figure(1)

data_sorted = np.sort(x)
p = 1. * np.arange(len(x)) / (len(x) - 1)

# plot the sorted data:
ax1 = f.add_subplot(121)
ax1.plot(data_sorted,p)
plt.title('CDF')
plt.xlabel('Datos')

f.show()

### Segundo gráfico ### Histograma - Normal
g = plt.figure(2)

plt.title('Histograma')
plt.xlabel('Datos')

n, bins, patches = plt.hist(x, bins='auto', alpha=0.5)
g.show()
