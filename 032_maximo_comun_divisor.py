# Write a Python program to compute the greatest common divisor (GCD) of two positive integers

def get_MCD(a,b):
    
    if a>b:
        mayor=a
    else:
        mayor=b
    
    mcd=0 # Por si no hay ningun MCD
    for i in range(1,(mayor//2)+1):
        if a%i == 0 and b%i == 0:
            mcd = i
    
    return mcd

print("\nMAXIMO COMUN DIVISOR\n")

a=int(input("Ingrese un numero:"))
b=int(input("Ingrese otro numero:"))

MCD = get_MCD(a,b)

if MCD != 0:
    print("El maximo comun divisor es:",MCD)
else:
    print("No existe MCD")

"""
MAXIMO COMUN DIVISOR

Ingrese un numero: 68
Ingrese otro numero: 102
El maximo comun divisor es: 34
"""
