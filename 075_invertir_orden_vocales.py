# Write a Python program to reverse only the vowels of a given string. Go to the editor

v = ['a','e','i','o','u']
s = input("Ingresar palabra, se invertira el orden de las vocales:")

st = s.lower()

print("Original:",st)

lst=list(st)

vocal_index = [i for i in range(len(lst)) if lst[i] in v]
vocal = [i for i in lst if i in v]

vocal.reverse()

cont=0
for i in vocal_index:
    lst[i]=vocal[cont]
    cont+=1

s = ''.join(lst)
print("Final:",s)

"""
Ingresar palabra, se invertira el orden de las vocales: Alejandro
Original: alejandro
Final: olajendra
"""
