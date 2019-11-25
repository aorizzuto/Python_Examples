# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y 
# lo almacene en una variable, y muestre por pantalla la frase "Tu índice de masa corporal es <imc>"
# donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

peso=input("Ingrese el peso en kg:")
altura=input("Ingrese la altura en m:")
imc=(float(peso)/(float(altura)**2))

print("Tu indice de masa corporal es {}".format(round(imc,2)))

"""
Ingrese el peso en kg: 80
Ingrese la altura en m: 1.8
Tu indice de masa corporal es 24.69
"""
