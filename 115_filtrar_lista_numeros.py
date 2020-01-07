
# Filtrar lista, solo numeros

def filter_list(lst):
	return [i for i in lst if isinstance(i, str)==0]
