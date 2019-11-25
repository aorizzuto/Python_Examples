# Almacenar una contraseña en una variable, pregunte al usuario por la contraseña e imprima si la contraseña coincide con la guardada sin tener en cuenta mayúsculas y minúsculas.
pass1=input("Introduzca la contraseña patron:")

while True:
    pass2=input("Introduzca otra contraseña para comparar:")
    if pass1.upper()==pass2.upper():
        print("    Contraseña correcta")
        break
        
"""
Introduzca la contraseña patron: Ale1234
Introduzca otra contraseña para comparar: alejandro
Introduzca otra contraseña para comparar: aLe123
Introduzca otra contraseña para comparar: AlE1235
Introduzca otra contraseña para comparar: ale1234
    Contraseña correcta
"""
