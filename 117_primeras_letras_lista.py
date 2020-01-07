# primeras letras de palabras en lista

def society_name(friends):
	return (''.join([i[0] for i in (sorted(friends))])).upper()
  
"""
friends = ["Alejandro","Sebastian","Lucia"]

ASL
"""
