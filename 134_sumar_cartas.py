

# Dandole valores a las cartas, sumar las cartas

def count(deck):
	dicc={2:1,3:1,4:1,5:1,6:1,7:0,8:0,9:0,10:-1,"J":-1,"Q":-1,"K":-1,"A":-1}
	return sum([dicc.get(i) for i in deck])

