# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
edad=int(input("Introduzca su edad:"))

if edad > 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
-------------------------------------------------
Introduzca su edad: 33
Es mayor de edad
-------------------------------------------------

# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
# Si el divisor es cero el programa debe mostrar un error.
numero1=float(input("Ingrese numero 1"))
numero2=float(input("Ingrese numero 2"))

if numero2 == 0:
    print("Error: divisor igual a 0")
else:
    print("Division: {}".format(numero1/numero2))

-------------------------------------------------
Ingrese numero 1 5
Ingrese numero 2 0
Error: divisor igual a 0

Ingrese numero 1 10
Ingrese numero 2 3
Division: 3.3333333333333335
-------------------------------------------------

# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
print("Ya realizado en Ejercicios_1_10.py")
Ya realizado en Ejercicios_1_10.py


# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
edad=int(input("Ingrese edad:"))
ingresos=float(input("Ingrese ingresos (euros):"))

ingresos_max=1000
edad_max=16

if edad > edad_max and ingresos >= ingresos_max:
    print("Puede tributar")
else:
    print("No puede tributar")

-------------------------------------------------
Ingrese edad: 33
Ingrese ingresos (euros): 999
No puede tributar

Ingrese edad: 17
Ingrese ingresos (euros): 1000
Puede tributar
-------------------------------------------------

"""
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y 
el grupo B por elresto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
"""
nombre=input("Ingrese nombre:")
sexo=input("Ingrese sexo (F o M):")

if (nombre[0].upper() > 'N' and sexo == 'M') or (nombre[0].upper() < 'M' and sexo == 'F'):
    print("Grupo A")
else:
    print("Grupo B")

-------------------------------------------------
Ingrese nombre: Natalia
Ingrese sexo (F o M): F
Grupo B

Ingrese nombre: Omar
Ingrese sexo (F o M): M
Grupo A

Ingrese nombre: Belen
Ingrese sexo (F o M): F
Grupo A

Ingrese nombre: Claudio
Ingrese sexo (F o M): M
Grupo B
-------------------------------------------------
"""
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

Renta                  Tipo impositivo
Menos de 10000€        5%
Entre 10000€ y 20000€  15%
Entre 200000€ y 35000€ 20%
Entre 350000€ y 60000€ 30%
Más de 60000€          45%
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
"""
rentas=[10000,20000,35000,60000]
impositivo=[5,15,20,30,45]

renta=float(input("Renta anual:"))

i=0

while i < len(rentas):
    if renta < rentas[i]:
        break
    i+=1
    
print(f"Tipo impositivo: {impositivo[i]}%")

-------------------------------------------------
Renta anual: 60001
Tipo impositivo: 45%
-------------------------------------------------

# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido
edad=int(input("Ingrese edad:"))

for i in range(edad):
    print(i+1)

-------------------------------------------------
Ingrese edad: 10
1
2
3
4
5
6
7
8
9
10
-------------------------------------------------

# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
import math

lista=[]
num=int(input("Ingrese numero entero:"))

for i in range(math.ceil(num/2)):
    lista.append(i*2+1)

print(','.join(str(e) for e in lista))

-------------------------------------------------
Ingrese numero entero: 24
1,3,5,7,9,11,13,15,17,19,21,23
-------------------------------------------------

# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
num=[1,2,3,4,5,6,7,8,9,10]
lista=[]

for i in range(1,11):
    lista.clear()
    for j in range(1,11):
        lista.append(i*j)
    print('\t'.join(str(e) for e in lista))
    
-------------------------------------------------
1	2	3	4	5	6	7	8	9	10
2	4	6	8	10	12	14	16	18	20
3	6	9	12	15	18	21	24	27	30
4	8	12	16	20	24	28	32	36	40
5	10	15	20	25	30	35	40	45	50
6	12	18	24	30	36	42	48	54	60
7	14	21	28	35	42	49	56	63	70
8	16	24	32	40	48	56	64	72	80
9	18	27	36	45	54	63	72	81	90
10	20	30	40	50	60	70	80	90	100
-------------------------------------------------

# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
num=int(input("Ingrese numero entero:"))

ret=1

if num%2 == 1:
    ret = 0
    for i in range(2,num):
        #print("{} {}".format(num,i))
        if num%i == 0:
            ret=1
            break

if ret == 1:
    print("No es primo")
else:
    print("Es primo")

-------------------------------------------------
Ingrese numero entero: 23
Es primo
-------------------------------------------------
