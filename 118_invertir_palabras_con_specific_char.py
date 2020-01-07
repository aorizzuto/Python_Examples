# Invertir palabras que contengan un caracter especifico

def special_reverse(s, c):
	return ' '.join([i if c not in i else i[::-1] for i in (s.split())])
  
  
