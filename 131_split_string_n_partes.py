
# Partir string en "n" partes

def partition(txt, n):
	return [txt[i:i+n] for i in range(0,len(txt),n)]
