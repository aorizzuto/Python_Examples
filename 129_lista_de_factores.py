# Lista de factores. Cada anterior es factor del siguiente

def factor_chain(l):
	for i in range(len(l)-1):
		if l[i+1]%l[i]==0:
			continue
		else:
			return False
	return True
  
"""
[1,2,4,16,64] True
[1,3,9,18,24] False
"""
