# Verificar si la suma de los impares es igual o a los pares de un numero entero

def odds_vs_evens(num):
	lst = list(map(int,str(num)))
	odd = [i for i in lst if i%2!=0]
	even = [i for i in lst if i%2==0]
	return "odd" if sum(odd)>sum(even) else "equal" if sum(even)==sum(odd) else "even"
