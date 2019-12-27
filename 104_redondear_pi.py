# Redondear pi a "n" decimales
import numpy as np

def my_pi(n):
    return round(np.pi,n)

print(my_pi(3))
print(my_pi(10))
print(my_pi(14))

"""
3.142
3.1415926536
3.14159265358979
"""
