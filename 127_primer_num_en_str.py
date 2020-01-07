# Tomar el primer numero que aparezca del string

import re

def left_digit(num):
	return int(re.sub('[^0-9]+', '', num)[0])
