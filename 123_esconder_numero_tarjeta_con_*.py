# Esconder numero de tarjeta

def card_hide(card):
	return ''.join(["*"]*(len(card)-4)) + card[len(card)-4:]


"""
123456789

*****6789
"""
