
# Devolver los indices de las mayusculas en un string

def index_of_caps(word):
	l=[]
	for i in range(len(word)):
		if word[i].isupper():
			l.append(i)
	return l

