# Write a Python program to find the difference between the largest integer and the smallest integer which are created by 8 numbers from 0 to 9. The number that can be rearranged shall start with 0 as in 00135668

s = input("Ingrese un numero:")

l = list(s)

l_max = sorted(l, reverse = True)
l_min = sorted(l)

lmax=''.join(l_max)
lmin=''.join(l_min)

print(a)
