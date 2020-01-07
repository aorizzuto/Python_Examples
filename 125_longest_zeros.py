# Cantidad de ceros mas largo 10010100000101

def longest_zero(s):
	return (sorted(s.split("1"),reverse=True))[0]
  
"""
original:           10010100000101

luego del split:    00 0 00000 0

luego del sorted:   0 0 00 00000

luego del reverse:  00000 00 0 0

retorno [0]:        00000
"""
