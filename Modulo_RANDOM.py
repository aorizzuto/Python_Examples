# RANDOM MODULE

import random

random.seed() # Genera la semilla para generar el número aleatorio. En este caso, al no pasar parametros utiliza el reloj del sistema
print ("Randint 1 - ", random.randint(0,100))  # Numero aleatorio entre 0 y 100
print ("Randint 2 - ", random.randint(25,50))
print ("Randint 3 - ", random.randint(50,100))

lst = [0,1,2,3,4,5,6,7,8,9,10]
print ("Choice 1 - ", random.choice(lst))  # Elección de número dentro de una lista
print ("Choice 2 - ", random.choice(lst))
print ("Choice 3 - ", random.choice(lst))

state = random.getstate() # Guardo el estado

print(random.sample(range(20),k=10)) # *1*
print(random.sample(range(20),k=20))

random.setstate(state)       # Restauro el estado anterior

print(random.sample(range(20),k=10)) # Me vuelve a generar los mismos valores que en *1*
