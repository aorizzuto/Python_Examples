
# Mayusculas primero y luego minusculas

def cap_to_front(s):
	up = [i for i in s if i.isupper()]
	low = [i for i in s if i.islower()]
	return ''.join(up)+''.join(low)
  
"""
"ALejaNDro"
"ALNDejaro"
"""
