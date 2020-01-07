# Contar lower/upper 

def steps_to_convert(txt):
	low=0
	up=0
  
	for i in txt:
		if i.islower():
			low+=1
		else:
			up+=1
      
	return up if up<low else low
