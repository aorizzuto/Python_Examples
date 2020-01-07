

# Revertir parte de una lista s:start f:fin

def ranged_reversal(lst, s, f):
	return lst[:s] + lst[s:f+1][::-1] + lst[f+1:]

