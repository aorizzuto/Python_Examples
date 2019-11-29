# Write a Python program to find the median among "n" given numbers

num=[9,5,18,2,4,3,13,25,1,8,2]
print("Lista 1:",num)

num.sort()
print("Lista 1 ordenada:",num)

if len(num)%2:
    print("\tNumero impar de datos. Mediana =",num[len(num)//2])
else:
    print("\tNumero par de datos. Mediana =",(num[len(num)//2]+num[(len(num)//2)+1])/2)

"""
Lista 1: [9, 5, 18, 2, 4, 3, 13, 25, 1, 8, 2]
Lista 1 ordenada: [1, 2, 2, 3, 4, 5, 8, 9, 13, 18, 25]
	Numero impar de datos. Mediana = 5
"""
