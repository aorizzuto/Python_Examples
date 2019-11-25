# Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged

print("\n¿STRING EMPIEZA CON \"IS\"?")

for i in range(2):
    string=input("\nEscribir una oracion:")

    str=string[0]+string[1]

    if str.upper() == "IS":
        print(string)
    else:
        string=string[:1].lower()+string[1:]
        print("Is",string)

"""
¿STRING EMPIEZA CON "IS"?
Escribir una oracion: Is there a house?
Is there a house?
Escribir una oracion: The penguin is called Alberto
Is the penguin is called Alberto
"""
