
# Convertir porcentajes en numeros

def convert_to_decimal(perc):
	return [float(i.split('%')[0])/100 for i in perc]
