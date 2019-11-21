# Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
print("¡Hola Mundo!")
--------------------------------------------------------
¡Hola Mundo!
--------------------------------------------------------

# Escribir un programa que almacene ¡Hola Mundo! y luego muestre por pantalla el contenido
hola_mundo="¡Hola Mundo!"
print(hola_mundo)
--------------------------------------------------------
¡Hola Mundo!
--------------------------------------------------------

# Escribir un programa que pregunte el nombre del usuario y después muestre por pantalla la cadena ¡Hola <nombre>!
nombre=input("Introduzca el nombre")
print(f"¡Hola {nombre}!")
--------------------------------------------------------
Introduzca el nombre Alejandro
¡Hola Alejandro!
--------------------------------------------------------

# Escribir un programa que pregunte el nombre del usuario y un número entero e imprima, en líneas distintas, el nombre del usuario tantas veces como el número introducido.
nombre=input("Introduzca el nombre: ")
numero=input("Numero de repetición: ")

for i in range(int(numero)):
    print(nombre)

--------------------------------------------------------
Introduzca el nombre:  Ale
Numero de repetición:  3
Ale
Ale
Ale
--------------------------------------------------------

# Escribir un programa que pregunte el nombre del usuario y luego muestre por pantalla <NOMBRE> tiene <n> letras, 
# donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.

nombre=input("Introduzca el nombre:")
print(f"{nombre.upper()} tiene {len(nombre)} letras")

--------------------------------------------------------
Introduzca el nombre: Alejandro
ALEJANDRO tiene 9 letras
--------------------------------------------------------

# Escribir un programa que realice la siguiente operación aritmética ((3+2)/(2⋅5))2
print(((3+2)/(2-5))**2)

--------------------------------------------------------
2.777777777777778
--------------------------------------------------------

# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y 
# lo almacene en una variable, y muestre por pantalla la frase "Tu índice de masa corporal es <imc>"
# donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

peso=input("Ingrese el peso en kg:")
altura=input("Ingrese la altura en m:")
imc=(float(peso)/(float(altura)**2))

print("Tu indice de masa corporal es {}".format(round(imc,2)))

--------------------------------------------------------
Ingrese el peso en kg: 80
Ingrese la altura en m: 1.8
Tu indice de masa corporal es 24.69
--------------------------------------------------------

# Escribir un programa que pida al usuario dos números enteros y muestre "<n> entre <m> da un cociente <c> y un resto <r>"
n1=input("Ingrese numero 1:")
n2=input("Ingrese numero 2:")

numero1=float(n1)
numero2=float(n2)

print("{} entre {} da un cociente {} y resto {}".format(numero1,numero2,numero1//numero2,numero1%numero2))

--------------------------------------------------------
Ingrese numero 1: 18
Ingrese numero 2: 5
18.0 entre 5.0 da un cociente 3.0 y resto 3.0
--------------------------------------------------------

# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y 
# muestre por pantalla el capital obtenido en la inversión.
inversion = float(input("Cantidad a invertir:"))
interes = float(input("Interes anual:"))
ano = int(input("Años:"))

print(f"Capital final: {round(inversion * (interes / 100 + 1) ** ano, 2)}")

--------------------------------------------------------
Cantidad a invertir: 2000
Interes anual: 5
Años: 2
Capital final: 2205.0
--------------------------------------------------------

# Almacenar una contraseña en una variable, pregunte al usuario por la contraseña e imprima si la contraseña coincide con la guardada sin tener en cuenta mayúsculas y minúsculas.
pass1=input("Introduzca la contraseña patron:")

while True:
    pass2=input("Introduzca otra contraseña para comparar:")
    if pass1.upper()==pass2.upper():
        print("    Contraseña correcta")
        break
        
--------------------------------------------------------
Introduzca la contraseña patron: Ale1234
Introduzca otra contraseña para comparar: alejandro
Introduzca otra contraseña para comparar: aLe123
Introduzca otra contraseña para comparar: AlE1235
Introduzca otra contraseña para comparar: ale1234
    Contraseña correcta
--------------------------------------------------------
