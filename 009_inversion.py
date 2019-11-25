# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y 
# muestre por pantalla el capital obtenido en la inversión.

inversion = float(input("Cantidad a invertir:"))
interes = float(input("Interes anual:"))
ano = int(input("Años:"))

print(f"Capital final: {round(inversion * (interes / 100 + 1) ** ano, 2)}")

"""
Cantidad a invertir: 2000
Interes anual: 5
Años: 2
Capital final: 2205.0
"""
