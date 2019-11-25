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

"""
Renta anual: 60001
Tipo impositivo: 45%
"""
