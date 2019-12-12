def even_odd_partition(lst):
	return [[i for i in lst if i%2 == 0],[i for i in lst if i%2 != 0]]
