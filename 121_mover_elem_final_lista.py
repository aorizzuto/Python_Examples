
# Mover elemento al final de la lista

def move_to_end(lst, el):
	for i in range(lst.count(el)):
		lst.remove(el)
		lst.append(el)
	return lst
