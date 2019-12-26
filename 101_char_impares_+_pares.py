# Retornar caracteres en posiciones pares concatenados a los de las posiciones impares
def index_shuffle(txt):
	lst1 = ''.join([txt[i] for i in range(len(txt)) if i%2==0])
	lst2 = ''.join([txt[i] for i in range(len(txt)) if i%2!=0])
	return lst1+lst2
  
print(index_shuffle("alejandro")
  
"""
aeadoljnr
"""
