# Hay dos letras consecutivas iguales?

def double_letters(w):
	for i in range(len(w)-1):
		if w[i] == w[i+1]:
			return True
	return False
