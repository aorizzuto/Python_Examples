

# verificar si la segunda palabra de la lista está contenida en la primera

def letter_check(lst):
	return all([i in (lst[0]).lower() for i in (lst[1]).lower()])

