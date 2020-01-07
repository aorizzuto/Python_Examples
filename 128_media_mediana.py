# Calcular la media de los digitos de un numero

def mean(num):
	x=list(map(int,str(num)))
	return sum(x)/len(x)
  
  

# Mediana de una lista

def median(lst):
	lst.sort()
	le=len(lst)
	if le%2 != 0:
		return lst[le//2]
	else:
		return ((lst[le//2] - lst[le//2 - 1])/2) + lst[le//2 -1]
	
	# another way
	# import statistics
	# statistics.median(lst)
