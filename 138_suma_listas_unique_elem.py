
# Si la suma de dos listas termina teniendo el mismo elemento
# [1,2,3,4,5]
# [5,4,3,2,1]
#     =
# [6,6,6,6,6] -> True

def puzzle_pieces(a1, a2):
	try:
		return len(set([a1[i]+a2[i] for i in range(len(a1))]))==1 and len(a1)==len(a2)
	except:
		return False
