# RANDOM MODULE

import random 

#-------------------------------------------------------------------------
# Bookkeeping functions (SEED/GETSTATE/SETSTATE/GETRANDBIT)
    # SEED
random.seed() # Genera la semilla para generar el número aleatorio. En este caso, al no pasar parametros utiliza el reloj del sistema

    # GETSTATE / SETSTATE
state = random.getstate() # Guardo el estado
print("\nGuardé el estado:")
print(random.sample(range(20),k=10)) # *1*
print(random.sample(range(20),k=20))
print("Restauré el estado:")
random.setstate(state)       # Restauro el estado anterior

print(random.sample(range(20),k=10)) # Me vuelve a generar los mismos valores que en *1*

    # GETRANDBIT

print("\nGetrandbits(bits:2):", random.getrandbits(2)) # Entrega un "int" que se pueda formar con la cantidad de bits. Ej: n=2 --> 00,01,10,11 (0,1,2,3)





#-------------------------------------------------------------------------
# Functions for integers (randrange/randint)

    # RANDRANGE
print("\nRandrange(stop:10):", random.randrange(10))
print("Randrange(start:10,stop:20,step:2):", random.randrange(10,20,2))

    # RANDINT
print ("\nRandint(0,100):", random.randint(0,100))  # Numero aleatorio entre 0 y 100
print ("Randint(25,50):", random.randint(25,50))
print ("Randint(50,100):", random.randint(50,100))





#-------------------------------------------------------------------------
# Functions for sequences (Choice/Shuffle/Sample)

    # CHOICE
lst = [0,1,2,3,4,5,6,7,8,9,10]
print("\nLista:",lst)
print ("Choice 1:", random.choice(lst))  # Elección de número dentro de una lista
print ("Choice 2:", random.choice(lst))
print ("Choice 3:", random.choice(lst))

    # SHUFFLE
print("\nLista antes de Shuffle:",lst)
random.shuffle(lst)
print("Lista después de Shuffle:",lst)

    # SAMPLE
lst = [0,1,2,3,4,5,6,7,8,9,10]
print("\nLista:",lst)
print("Sample(lst,4):",random.sample(lst,4))





#-------------------------------------------------------------------------
# Real-valued distributions

    # RANDOM  (Toma valores float entre 0.0 y 1.0)
print("\nRandom():",random.random())

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
Guardé el estado:
[16, 2, 13, 1, 11, 8, 19, 3, 6, 12]
[14, 9, 1, 13, 6, 12, 2, 5, 7, 4, 8, 18, 3, 11, 10, 19, 17, 0, 16, 15]
Restauré el estado:
[16, 2, 13, 1, 11, 8, 19, 3, 6, 12]

Getrandbits(bits:2): 1

Randrange(stop:10): 4
Randrange(start:10,stop:20,step:2): 18

Randint(0,100): 7
Randint(25,50): 38
Randint(50,100): 63

Lista: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Choice 1: 2
Choice 2: 5
Choice 3: 7

Lista antes de Shuffle: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Lista después de Shuffle: [6, 2, 0, 1, 5, 10, 7, 3, 9, 8, 4]

Lista: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Sample(lst,4): [10, 6, 3, 8]

Random(): 0.45089932715349834

Uniform(min:1.2,max:2.5): 1.268337621198389

Triangular(low:1,high:2,mas cerca de:1): 1.0792895723041276

Distribución Beta - betavariate(2,5): 0.11933032947270282

Distribución Exponencial - expovariate(2): 0.42615910897006665

Distribución Gamma - gammavariate(alpha:1,beta:3): 5.4593025051283055

Distribución Gamma - gauss(mu:1,sigma:3): 0.7264765186877808

Distribución Log - gauss(mu:1,sigma:3): 19.842793992182138

Distribución Normal - gauss(mu:1,sigma:3): 2.038581137814786

Distribución Vonmises - gauss(mu:1,kappa:3): 1.5531342843611993

Distribución Pareto - gauss(alpha:1): 1.4111196126979926

Distribución Weibull - gauss(alpha:1,beta:3): 1.0078672935069248
"""
