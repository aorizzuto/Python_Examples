
# Devolver la cantidad de veces que se repite un numero entre 3

def equal(a, b, c):
	return 4 - len(set([a,b,c])) if len(set([a,b,c]))!=3 else 0

